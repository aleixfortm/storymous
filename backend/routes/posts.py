from flask import jsonify, request
from bson import json_util
from flask_pymongo import ObjectId
from flask import Blueprint, jsonify
from main import db_posts, db_users, db_comments, db_chapters
from models.models import PostModel, UserModel, CommentModel, ChapterModel
from models.chapter import Chapter
from models.story import Story
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from werkzeug.security import check_password_hash, generate_password_hash
from pprint import pprint
from datetime import timedelta
import random

# misc data
post_dict = {}

# create blueprint
bp_posts = Blueprint('posts', __name__)


def add_to_db(post_list):
    for post in post_list:
        if post["type"] == "chapter":

            chapter_obj = Chapter(_id=post["_id"], story_id=story_id, created_at=post["date"], username=post["username"], title=post["title"], content=post["content"], comment=post["comment"], views=post["views"], tags=post["tags"], leaves=post["leaves"], chapter_num=0)
            chapter_obj.save_to_db()


# sanity check route
@bp_posts.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


# create new post sequence
@bp_posts.route('/new_post', methods=['POST'])
@jwt_required()
def new_post():
    post = request.json
    post_req_data = {
        "comment": post.get("comment"),
        "title": post.get("title"),
        "content": post.get("body"),
        "username": post.get("username"),
        "tags": post.get("tags"),
        "leaves": [post.get("username")]
    }

    post_object = PostModel(**post_req_data)
    post_object.add_html_line_jumps()
    post_object.quicksave_to_db()

    UserModel.increase_leaves(post["username"])
    UserModel.update_started_story_count(post["username"])

    return json_util.dumps({"status": "Success"})


# create new comment sequence
@bp_posts.route('/new_comment', methods=['POST'])
@jwt_required()
def new_pcomment():
    comment = request.json
    comment_req_data = {
        "comment": comment.get("comment"),
        "username": comment.get("username"),
    }

    comment_object = CommentModel(**comment_req_data)
    comment_object.quicksave_to_db()

    CommentModel.add_to_parent(comment["parentId"], comment_object.__dict__)

    # convert object to dict
    comment_dict = comment_object.__dict__
    PostModel.format_date_data(comment_dict)
    query = {"username": comment["username"]}
    user_data = db_users.find_one(query)
    comment_dict["picture"] = user_data["picture"]

    data_payload = {
        "status": "Success",
        "comment_data": comment_dict
    }

    return json_util.dumps(data_payload)


# get all posts
@bp_posts.route('/posts', methods=["GET"])
def posts():
    post_list = list(db_posts.find())
    post_list.extend(list(db_chapters.find()))
    sorted_post_list = sorted(post_list, key=lambda x: x["date"])

    #add_to_db(post_list)

    for post in sorted_post_list:
        PostModel.format_date_data(post)
        user = db_users.find_one({"username": post["username"]})
        post["picture"] = user["picture"]
    
    post_dict["latest"] = sorted_post_list[::-1]
    post_dict["following"] = []

    return json_util.dumps(post_dict)


# get all posts
@bp_posts.route('/homepage_posts/<user>', methods=["GET"])
def posts_logged_in(user):

    post_list = list(db_posts.find())
    post_list.extend(list(db_chapters.find()))
    sorted_post_list = sorted(post_list, key=lambda x: x["date"])

    for post in sorted_post_list:
        PostModel.format_date_data(post)
        user_fetched_data = db_users.find_one({"username": post["username"]})
        post["picture"] = user_fetched_data["picture"]
    post_dict["latest"] = sorted_post_list[::-1]

    user_query = {"username": user}
    user_data = db_users.find_one(user_query)

    # if user does not follow anyone, return empty list
    if not user_data["following"]:
        post_dict["following"] = []
        return json_util.dumps(post_dict)

    # if the user follows other users
    following_query = {"username": {"$in": user_data["following"]}}
    post_list = list(db_posts.find(following_query))
    post_list.extend(list(db_chapters.find(following_query)))
    sorted_post_list = sorted(post_list, key=lambda x: x["date"])

    for post in post_list:
        PostModel.format_date_data(post)
        user_fetched_data_fol = db_users.find_one({"username": post["username"]})
        post["picture"] = user_fetched_data_fol["picture"]
    post_dict["following"] = post_list[::-1]

    return json_util.dumps(post_dict)


# get user posts
@bp_posts.route("/posts/<user>", methods=["GET"])
def user_posts(user):

    post_list = list(db_posts.find({"username": user}))
    post_list.extend(list(db_chapters.find({"username": user})))
    sorted_post_list = sorted(post_list, key=lambda x: x["date"])

    for post in sorted_post_list:
        PostModel.format_date_data(post)
        user_fetched_data = db_users.find_one({"username": post["username"]})
        post["picture"] = user_fetched_data["picture"]
        
    return json_util.dumps(sorted_post_list[::-1])


@bp_posts.route("/add_leaves_post", methods=["POST"])
@jwt_required()
def add_leaves_post():
    data = request.json
    PostModel.increase_leaves(data["post_id"], data["username"])
    UserModel.increase_leaves(data["username_receiver"])

    data_payload = {
        "status": "Success",
    }

    return json_util.dumps(data_payload)


@bp_posts.route("/add_leaves_chapter", methods=["POST"])
@jwt_required()
def add_leaves_chapter():
    data = request.json
    ChapterModel.increase_leaves(data["chapter_id"], data["username"])
    UserModel.increase_leaves(data["username_receiver"])

    data_payload = {
        "status": "Success",
    }

    return json_util.dumps(data_payload)


@bp_posts.route("/remove_leaves_post", methods=["POST"])
@jwt_required()
def remove_leaves_post():
    data = request.json
    PostModel.decrease_leaves(data["post_id"], data["username"])
    UserModel.decrease_leaves(data["username_receiver"])

    data_payload = {
        "status": "Success",
    }

    return json_util.dumps(data_payload)


@bp_posts.route("/remove_leaves_chapter", methods=["POST"])
@jwt_required()
def remove_leaves_chapter():
    data = request.json
    ChapterModel.decrease_leaves(data["chapter_id"], data["username"])
    UserModel.decrease_leaves(data["username_receiver"])

    data_payload = {
        "status": "Success",
    }

    return json_util.dumps(data_payload)


### NO MORE FROM HERE ###


# get chapter by id
@bp_posts.route("/chapter/<chapterId>", methods=["GET"])
def chapter(chapterId):

    # search for chapter data
    chapter_query = {"_id": ObjectId(chapterId)}
    chapter_data = db_chapters.find_one(chapter_query)
    ChapterModel.increase_visits(chapterId)

    # find story prologue
    chapter_list = []
    story_query = {"_id": chapter_data["story_id"]}
    prologue_data = db_posts.find_one(story_query)
    user_query = {"username": prologue_data["username"]}
    user_data = db_users.find_one(user_query)
    prologue_data["picture"] = user_data["picture"]
    PostModel.format_date_data(prologue_data)
    PostModel.increase_visits(prologue_data["_id"])

    # iterate through parent chapters until it reaches chapter 1
    for _ in range(chapter_data["chapter_num"]): 
        # find user data to add picture to each post
        user_query = {"username": chapter_data["username"]}
        user_data = db_users.find_one(user_query)
        chapter_data["picture"] = user_data["picture"]
        PostModel.format_date_data(chapter_data)
        chapter_list.insert(0, chapter_data)
        # find parent chapter to keep looping and adding chapters to list
        parent_chapter_query = {"_id": chapter_data["parent_chapter_id"]}
        parent_chapter_data = db_chapters.find_one(parent_chapter_query)
        chapter_data = parent_chapter_data
    
    # add prologue to first positionvisits
    chapter_list.insert(0, prologue_data)
    return json_util.dumps(chapter_list)


# get post by id
@bp_posts.route("/post/<postId>", methods=["GET"])
def post(postId):

    post_data = {}
    query = {"_id": ObjectId(postId)}
    post = db_posts.find_one(query)
    query = {"username": post["username"]}
    user_data = db_users.find_one(query)
    post["picture"] = user_data["picture"]
    PostModel.format_date_data(post)
    post_data["post"] = post
    PostModel.increase_visits(post["_id"])

    replies = []
    for comment_id in post["user_comments"]:
        query = {"_id": comment_id}
        comment_data = db_comments.find_one(query)
        if comment_data:
            query = {"username": comment_data["username"]}
            user_data = db_users.find_one(query)
            comment_data["picture"] = user_data["picture"]
            replies.append(comment_data)
    
    chapter_query = {"story_id": post["_id"]}
    chapters_list = list(db_chapters.find(chapter_query))
    for chapter in chapters_list:
        query = {"username": chapter["username"]}
        user_data = db_users.find_one(query)
        chapter["picture"] = user_data["picture"]


    replies.extend(chapters_list)
    replies = sorted(replies, key=lambda x: x["date"])
    for reply in replies:
        PostModel.format_date_data(reply)

    post_data["replies"] = replies[::-1]

    return json_util.dumps(post_data)


@bp_posts.route("/new_chapter", methods=["POST"])
@jwt_required()
def new_chapter():

    # gather data from POST request and place it into a dictionary
    data = request.json
    chapter_data = {
        "story_id": ObjectId(data["storyId"]),
        "parent_chapter_id": ObjectId(data["parentChapterId"]),
        "username": data["username"],
        "chapter_name": data["title"],
        "chapter_num": data["chapterNum"],
        "content": data["body"],
        "comment": data["comment"],
        "tags": data["tags"],
        "leaves": [data["username"]]
    }

    UserModel.increase_leaves(data["username"])

    # create chapter object from chapter model schema and save it to db
    chapter_object = ChapterModel(**chapter_data)
    chapter_object.quicksave_to_db()

    # create data packet containing status message and chapter_id of the newly created chapter
    data_packet = {
        "status": "Success",
        "chapter_id": chapter_object._id
    }

    # if there was a problem with object construction, _id will not exist, therefore send failed status
    if not data_packet.get("chapter_id"):
        return json_util.dumps({"status": "failed"})
    
    # else send the previously stablished data packet
    return json_util.dumps(data_packet)

