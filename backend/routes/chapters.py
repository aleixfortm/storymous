from flask import jsonify, request
from bson import json_util
from flask_pymongo import ObjectId
from flask import Blueprint, jsonify
from main import db_users, db_comments, db_stories, db_chapters2
from models.chapter import Chapter
from models.user import User
from models.comment import Comment
from models.story import Story
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from pprint import pprint
from datetime import timedelta
import random

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
        "content": chapter.get("body"),
        "username": chapter.get("username"),
        "tags": chapter.get("tags"),
        "chapter_num": chapter.get("chapterNum") or 0,
        "leaves": [chapter.get("username")]
    }

    chapter_object = Chapter(**chapter_data)
    chapter_object.save_to_db()
    # increase written story count of user
    chapter_object.increase_user_written_stories() # author leaf is automatically added when creating the object
    User.increase_leaves(chapter["username"])

    return json_util.dumps({"status": "Success"})


# get all chapters (LOGGED OUT)
@bp_chapters.route('/chapters', methods=["GET"])
def chapters():

    chapter_list = list(db_chapters2.find())
    sorted_chapters = sorted(chapter_list, key=lambda x: x["created_at"])

    for chapter in sorted_chapters:
        Chapter.format_date_data(chapter["created_at"])
        user = db_users.find_one({"username": chapter["username"]})
        chapter["picture"] = user["picture"]
    
    chapter_dict = {}
    chapter_dict["latest"] = sorted_chapters[::-1]
    chapter_dict["following"] = []

    return json_util.dumps(chapter_dict)


# get all chapters (LOGGED IN)
@bp_chapters.route('/homepage_chapters/<requested_user>', methods=["GET"])
def posts_logged_in(requested_user):

    chapter_list = list(db_chapters2.find())
    sorted_chapters = sorted(chapter_list, key=lambda x: x["created_at"])

    for chapter in sorted_chapters:
        Chapter.format_date_data(chapter["created_at"])
        user = db_users.find_one({"username": chapter["username"]})
        chapter["picture"] = user["picture"]
    
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
    chapter_list = list(db_chapters2.find(following_query))
    sorted_chapters = sorted(chapter_list, key=lambda x: x["created_at"])

    for chapter in sorted_chapters:
        Chapter.format_date_data(chapter["created_at"])
        user = User.find_by_username(chapter["username"])
        chapter["picture"] = user["picture"]

    chapter_dict["following"] = sorted_chapters[::-1]

    return json_util.dumps(chapter_dict)


# get user posts
@bp_chapters.route("/chapters/<requested_user>", methods=["GET"])
def user_posts(requested_user):

    chapter_list = list(db_chapters2.find({"username": requested_user}))
    sorted_chapters = sorted(chapter_list, key=lambda x: x["created_at"])

    for chapter in sorted_chapters:
        Chapter.format_date_data(chapter["created_at"])
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