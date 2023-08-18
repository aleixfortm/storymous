from flask import jsonify, request
from bson import json_util
from flask_pymongo import ObjectId
from flask import Blueprint, jsonify
from main import db_users, db_comments, db_chapters, db_stories
from models.chapter import Chapter
from models.user import User
from models.comment import Comment
from models.story import Story
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from pprint import pprint


# create blueprint
bp_chapters = Blueprint('chapters', __name__)


# create new chapter
@bp_chapters.route('/new_chapter', methods=['POST'])
@jwt_required()
def new_chapter():
    chapter = request.json
    chapter_data = {
        "comment": chapter.get("comment"),
        "title": chapter.get("title"),
        "content": chapter.get("content"),
        "username": chapter.get("username"),
        "tags": chapter.get("tags"),
        "chapter_num": chapter.get("chapter_num"),
        "leaves": [chapter.get("username")],
        "story_id": chapter.get("story_id"),
        "parent_id": chapter.get("parent_id")
    }

    # if no story_id (new story), 
    if not chapter_data.get("story_id"):
        # create a new Story instance
        story_object = Story(title=chapter_data["title"])
        # update chapter_data object
        chapter_data["story_id"] = story_object._id
        # create Chapter instance with updated story_id values and save it do db
        chapter_object = Chapter(**chapter_data)
        # add chapter _id to story
        story_object.chapters = [chapter_object._id]
        # increase written story count of user
        chapter_object.increase_user_written_stories() # author leaf is automatically added when creating the object
        # increase amount of leaves of author, as they are automatically added
        User.increase_leaves(chapter_object.username)
        # save both instances to db
        chapter_object.save_to_db()
        story_object.save_to_db()

    else: # if there is story_id (chapter_num > 0) -> Continuation
        # create chapter instance
        chapter_object = Chapter(**chapter_data)
        # increase user's number of written chapters
        chapter_object.increase_user_written_stories()
        # save chapter to db
        chapter_object.save_to_db()
        # add chapter id to respective story
        chapter_object.save_to_stories()

    data_packet = {
        "status": "Success",
        "chapter": chapter_object.__dict__
    }

    return json_util.dumps(data_packet)


# get all chapters (LOGGED OUT)
@bp_chapters.route('/chapters', methods=["GET"])
def chapters():

    chapter_list = list(db_chapters.find())
    sorted_chapters = sorted(chapter_list, key=lambda x: x["created_at"])

    for chapter in sorted_chapters:
        chapter["created_at"] = Chapter.format_date_data(chapter["created_at"])
        user = db_users.find_one({"username": chapter["username"]})
        chapter["picture"] = user["picture"]
        story = db_stories.find_one({"_id": chapter["story_id"]})
        chapter["story_name"] = story["title"]
        chapter["comments"] = story["comments"]

    chapter_dict = {}
    chapter_dict["latest"] = sorted_chapters[::-1]
    chapter_dict["following"] = []

    return json_util.dumps(chapter_dict)


# get all chapters (LOGGED IN)
@bp_chapters.route('/homepage_chapters/<requested_user>', methods=["GET"])
def posts_logged_in(requested_user):

    chapter_list = list(db_chapters.find())
    sorted_chapters = sorted(chapter_list, key=lambda x: x["created_at"])

    for chapter in sorted_chapters:
        chapter["created_at"] = Chapter.format_date_data(chapter["created_at"])
        user = db_users.find_one({"username": chapter["username"]})
        chapter["picture"] = user["picture"]
        story = db_stories.find_one({"_id": chapter["story_id"]})
        chapter["story_name"] = story["title"]
        chapter["comments"] = story["comments"]
    
    chapter_dict = {}
    chapter_dict["latest"] = sorted_chapters[::-1]

    user_query = {"username": requested_user}
    user = db_users.find_one(user_query)

    # if user does not follow anyone, return empty list
    if not user["following"]:
        chapter_dict["following"] = []
        return json_util.dumps(chapter_dict)

    # if the user follows other users
    following_query = {"username": {"$in": user["following"]}}
    chapter_list = list(db_chapters.find(following_query))
    sorted_chapters = sorted(chapter_list, key=lambda x: x["created_at"])

    for chapter in sorted_chapters:
        chapter["created_at"] = Chapter.format_date_data(chapter["created_at"])
        user = User.find_by_username(chapter["username"])
        chapter["picture"] = user["picture"]
        story = db_stories.find_one({"_id": chapter["story_id"]})
        chapter["story_name"] = story["title"]
        chapter["comments"] = story["comments"]

    chapter_dict["following"] = sorted_chapters[::-1]

    return json_util.dumps(chapter_dict)


# get chapter by id
@bp_chapters.route("/chapter/<chapterId>", methods=["GET"])
def chapter(chapterId):

    # search for chapter data
    chapter_query = {"_id": ObjectId(chapterId)}
    chapter_data = db_chapters.find_one(chapter_query)
    user_data = User.find_by_username(chapter_data["username"])
    chapter_data["created_at"] = Chapter.format_date_data(chapter_data["created_at"])
    chapter_data["picture"] = user_data["picture"]
    Chapter.increase_visits(chapterId)
    storyline = [chapter_data]
    story_query = {"_id": chapter_data["story_id"]}
    story_data = db_stories.find_one(story_query)

    # add every parent chapter to the list
    if chapter_data["parent_id"]:
        while True:
            parent_chapter_query = {"_id": chapter_data["parent_id"]}
            chapter_data = db_chapters.find_one(parent_chapter_query)
            user_data = User.find_by_username(chapter_data["username"])
            chapter_data["created_at"] = Chapter.format_date_data(chapter_data["created_at"])
            chapter_data["picture"] = user_data["picture"]
            storyline.insert(0, chapter_data)
            if chapter_data["parent_id"] == None:
                break
    
    # query all chapters present in chapters list of story instance, but exclude those whose parent_id is None (chapter 0)
    all_chapters = list(db_chapters.find(
        {"_id": {"$in": story_data["chapters"]},
        "parent_id": {"$ne": None}
    }))
    for chapter in all_chapters:
        user_data = User.find_by_username(chapter["username"])
        chapter["picture"] = user_data["picture"]
        chapter["created_at"] = Chapter.format_date_data(chapter["created_at"])

    comments = list(db_comments.find({"_id": {"$in": story_data["comments"]}}))
    for comment in comments:
        user_data = User.find_by_username(comment["username"])
        comment["picture"] = user_data["picture"]
        comment["date"] = Chapter.format_date_data(comment["date"])

    data_packet = {
        "mountedChapters": storyline,
        "allChapters": all_chapters,
        "comments": comments[::-1]
    }

    return json_util.dumps(data_packet)


# get user posts
@bp_chapters.route("/chapters/<requested_user>", methods=["GET"])
def user_posts(requested_user):

    chapter_list = list(db_chapters.find({"username": requested_user}))
    sorted_chapters = sorted(chapter_list, key=lambda x: x["created_at"])

    for chapter in sorted_chapters:
        chapter["created_at"] = Chapter.format_date_data(chapter["created_at"])
        user_dict = User.find_by_username(chapter["username"])
        chapter["picture"] = user_dict["picture"]
        
    return json_util.dumps(sorted_chapters[::-1])


@bp_chapters.route("/add_leaf_chapter", methods=["POST"])
@jwt_required()
def add_leaf_chapter():

    data = request.json

    Chapter.increase_leaves(data["chapter_id"], data["username"])
    User.increase_leaves(data["username_receiver"])

    return json_util.dumps({"status": "Success"})


@bp_chapters.route("/remove_leaf_chapter", methods=["POST"])
@jwt_required()
def remove_leaves_chapter():

    data = request.json

    Chapter.decrease_leaves(data["chapter_id"], data["username"])
    User.decrease_leaves(data["username_receiver"])

    return json_util.dumps({"status": "Success"})


# create new comment sequence
@bp_chapters.route('/new_comment', methods=['POST'])
@jwt_required()
def new_comment():
    comment = request.json
    comment_req_data = {
        "comment": comment.get("comment"),
        "username": comment.get("username"),
        "story_id": comment.get("story_id")
    }
    
    comment_object = Comment(**comment_req_data)
    comment_object.quicksave_to_db()

    Comment.add_to_story(comment.get("story_id"), comment_object._id)

    # convert object to dict
    comment_dict = comment_object.__dict__
    comment_dict["date"] = Chapter.format_date_data(comment_dict["date"])
    query = {"username": comment["username"]}
    user_data = db_users.find_one(query)
    comment_dict["picture"] = user_data["picture"]

    data_payload = {
        "status": "Success",
        "comment_data": comment_dict
    }

    return json_util.dumps(data_payload)