from flask import jsonify, request
from bson import json_util
from flask_pymongo import ObjectId
from flask import Blueprint, jsonify
from main import db_posts, db_users, db_comments, db_chapters
from models import PostModel, UserModel, CommentModel, ChapterModel
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from werkzeug.security import check_password_hash, generate_password_hash
from config import COLOR_LIST, IMAGE_LIST, TAG_LIST
from pprint import pprint
from datetime import timedelta
import random

# misc data
post_dict = {}

# create blueprint
bp_routes = Blueprint('routes', __name__)


# sanity check route
@bp_routes.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


# sign up sequence
@bp_routes.route("/signup", methods=["POST"])
def signup():
    credentials = request.json
    username = credentials.get("username")
    password = credentials.get('password')
    email = credentials.get("email")
    
    # check if username and email exist already
    username_query = {"username": username}
    username_result = db_users.find_one(username_query)
    email_query = {"email": email}
    email_result = db_users.find_one(email_query)
    # return error request if user exists
    data_packet = {}
    if username_result:
        data_packet["status"] = "Username already exists"
        return json_util.dumps(data_packet), 401
    elif email_result:
        data_packet["status"] = "Email already exists"
        return json_util.dumps(data_packet), 401
    
    # generate password hash from user password
    hashed_password = generate_password_hash(password)
    # generate user object
    user_object = UserModel(username=username, password_hash=hashed_password, email=email)
    user_object.quicksave_to_db()

    data_packet["status"] = "Success"
    return json_util.dumps(data_packet), 201


# log in sequence
@bp_routes.route('/login', methods=['POST'])
def login():
    credentials = request.json
    username = credentials.get('username')
    password = credentials.get('password')

    # retrieve user data from db
    username_query = {"username": username}
    user_data = db_users.find_one(username_query)
    # return error if non-existent
    if not user_data:
        return jsonify({'status': 'Invalid username'}), 401
    # check password
    hashed_password = user_data.get("password_hash")
    if not check_password_hash(hashed_password, password):
        return jsonify({'status': 'Incorrect password'}), 401
    
    # User authenticated
    access_token = create_access_token(identity=username, expires_delta=timedelta(hours=1))  # Generate JWT token
    # get user data
    retrieved_user_data = db_users.find_one({"username": username})
    # return data packet
    return json_util.dumps({"token": access_token,
                            "user_data": retrieved_user_data,
                            "status": "Success"}), 200


# load user data
@bp_routes.route("/user/<user>", methods=["GET"])
def user(user):
    post_list = list(db_posts.find({"username": user}))
    post_list.extend(list(db_chapters.find({"username": user})))
    sorted_post_list = sorted(post_list, key=lambda x: x["date"])

    for post in sorted_post_list:
        PostModel.format_date_data(post)
        user_fetched_data = db_users.find_one({"username": post["username"]})
        post["picture"] = user_fetched_data["picture"]
    
    user_data = db_users.find_one({"username": user})
    
    data_packet = {
        "user_data": user_data,
        "posts": sorted_post_list[::-1]
    }

    return json_util.dumps(data_packet)


# load user data
@bp_routes.route("/settings/<user>", methods=["GET"])
def get_settings(user):
    user_data = db_users.find_one({"username": user})
    settings_data = {
        "color": user_data["color"],
        "bio": user_data["bio"],
        "picture": user_data["picture"]
    }

    return json_util.dumps(settings_data)


# follow updates
@bp_routes.route('/follow', methods=['POST'])
@jwt_required()
def follow():
    data = request.json
    if data.get("action") == "follow":
        UserModel.add_follower(data.get("user_being_followed"), data.get("user_follows"))
        return json_util.dumps("Success")
    
    else:
        UserModel.remove_follower(data.get("user_being_followed"), data.get("user_follows"))
        return json_util.dumps("Success")


# create new post sequence
@bp_routes.route('/new_post', methods=['POST'])
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

    UserModel.update_started_story_count(post["username"])

    return json_util.dumps({"status": "Success"})


# create new comment sequence
@bp_routes.route('/new_comment', methods=['POST'])
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
@bp_routes.route('/posts', methods=["GET"])
def posts():
    post_list = list(db_posts.find())
    post_list.extend(list(db_chapters.find()))
    sorted_post_list = sorted(post_list, key=lambda x: x["date"])

    for post in sorted_post_list:
        PostModel.format_date_data(post)
        user = db_users.find_one({"username": post["username"]})
        post["picture"] = user["picture"]
    
    post_dict["latest"] = sorted_post_list[::-1]
    post_dict["following"] = []

    return json_util.dumps(post_dict)


# get all posts
@bp_routes.route('/homepage_posts/<user>', methods=["GET"])
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
@bp_routes.route("/posts/<user>", methods=["GET"])
def user_posts(user):

    post_list = list(db_posts.find({"username": user}))
    post_list.extend(list(db_chapters.find({"username": user})))
    sorted_post_list = sorted(post_list, key=lambda x: x["date"])

    for post in sorted_post_list:
        PostModel.format_date_data(post)
        user_fetched_data = db_users.find_one({"username": post["username"]})
        post["picture"] = user_fetched_data["picture"]
        
    return json_util.dumps(sorted_post_list[::-1])


@bp_routes.route("/add_leaves_post", methods=["POST"])
@jwt_required()
def add_leaves_post():
    data = request.json
    PostModel.increase_leaves(data["post_id"], data["username"])
    UserModel.increase_leaves(data["username_receiver"])

    data_payload = {
        "status": "Success",
    }

    return json_util.dumps(data_payload)


@bp_routes.route("/add_leaves_chapter", methods=["POST"])
@jwt_required()
def add_leaves_chapter():
    data = request.json
    ChapterModel.increase_leaves(data["chapter_id"], data["username"])
    UserModel.increase_leaves(data["username_receiver"])

    data_payload = {
        "status": "Success",
    }

    return json_util.dumps(data_payload)


@bp_routes.route("/remove_leaves_post", methods=["POST"])
@jwt_required()
def remove_leaves_post():
    data = request.json
    PostModel.decrease_leaves(data["post_id"], data["username"])
    UserModel.decrease_leaves(data["username_receiver"])

    data_payload = {
        "status": "Success",
    }

    return json_util.dumps(data_payload)


@bp_routes.route("/remove_leaves_chapter", methods=["POST"])
@jwt_required()
def remove_leaves_chapter():
    data = request.json
    ChapterModel.decrease_leaves(data["chapter_id"], data["username"])
    UserModel.decrease_leaves(data["username_receiver"])

    data_payload = {
        "status": "Success",
    }

    return json_util.dumps(data_payload)


# get chapter by id
@bp_routes.route("/chapter/<chapterId>", methods=["GET"])
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
@bp_routes.route("/post/<postId>", methods=["GET"])
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


@bp_routes.route("/update_settings", methods=["POST"])
@jwt_required()
def update_user_settings():
    data = request.json
    user_query = {"username": data["username"]}
    updated_settings = {
        "$set": {
            "picture": data["selectedImage"],
            "bio": data["selectedBio"],
            "color": data["selectedColor"]
        }
    }
    db_users.update_one(user_query, updated_settings)

    fetched_user_data = db_users.find_one({"username": data["username"]})

    return json_util.dumps({
        "status": "Success",
        "updated_user_data": fetched_user_data
    })


@bp_routes.route("/new_chapter", methods=["POST"])
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


"""
from collections import Counter
# edit posts
@bp_routes.route('/edit_stuff', methods=["GET"])
def posts_edit():
    user_counter = Counter()
    
    posts = list(db_posts.find())
    for post in posts:
        user_counter[post["username"]] += len(post["leaves"])

    chapters = list(db_chapters.find())
    for chapter in chapters:
        user_counter[chapter["username"]] += len(chapter["leaves"])

    user_dict = dict(user_counter)
    for user, leaves_count in user_counter.items():
        query = {"username": user}
        update_data = {"$set": {"leaves": leaves_count}}
        db_users.update_one(query, update_data)
        
    return "Success"
"""

from collections import Counter
# edit posts
@bp_routes.route('/edit_stuff', methods=["GET"])
def edit_stuff():
    
    chapter_data = {
        "story_id": ObjectId("64396be8852aaec5dc1e4bfd"),
        "parent_chapter_id": ObjectId("64d61c7fc3f9a7a1f6f0ac7d"),
        "date": "2023-06-14T20:36:12.490426",
        "username": "benetti",
        "chapter_name": "The quest of CSGO pt.5",
        "chapter_num": 4,
        "content": "You know that feeling when good things are happenin' to you and you feel like you don't deserve it? That's me sitting in gold nova 2 right now... FUCK NO!!! I'M THE BEST!! I'm at my prime, when i thought i hit the cieling and i wasn't gettin' out of silver, BOOM! nova 1, and even when i thought that was it, DOUBLE BOOM! gold nova 2!! I have no words to describe my feelings, thankful for my pals who have been there when i was rock bottom and happy for all those haters who never gave me a chance! I'm coming for you S1mple!!",
        "comment": '“The harder the conflict, the greater the triumph.” - George Washington',
        "tags": ["fantasy", "young-adults", "humor", "chill"],
        "leaves": ["pixelated", "poll3", "astonished_98", "stoupeaks", "benetti"],
        "views": 160
    }

    chapter_obj = ChapterModel(**chapter_data)
    chapter_obj.quicksave_to_db()

        
    return "Success"