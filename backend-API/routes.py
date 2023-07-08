from flask import jsonify, request
from bson import json_util
from flask_pymongo import ObjectId
from flask import Blueprint, jsonify
from main import db_posts, db_users, db_comments, db_chapters
from models import PostModel, UserModel, CommentModel, ChapterModel
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from werkzeug.security import check_password_hash, generate_password_hash
from config import COLOR_LIST, IMAGE_LIST
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
    posts_list = list(db_posts.find({"username": user}))[::-1]
    for post in posts_list:
        user_data = db_users.find_one({"username": user})
        post["picture"] = user_data["picture"]
        PostModel.format_date_data(post)
    user_data = db_users.find_one({"username": user})

    return json_util.dumps({
                            "user_data": user_data,
                            "posts": posts_list
                            })


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
        "username": post.get("username")
    }

    post_object = PostModel(**post_req_data)
    post_object.add_html_line_jumps()
    post_object.quicksave_to_db()

    UserModel.update_post_count(post["username"])

    return json_util.dumps({"status": "Success"})


# create new post sequence
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
    for post in post_list:
        PostModel.format_date_data(post)
        user_data = db_users.find_one({"username": post["username"]})
        post["picture"] = user_data["picture"]
    post_dict["latest"] = post_list[::-1]

    user_query = {"username": user}
    user_data = db_users.find_one(user_query)

    # if user does not follow anyone, return empty list
    if not user_data["following"]:
        post_dict["following"] = []
        return json_util.dumps(post_dict)

    # if the user follows other users
    following_query = {"username": {"$in": user_data["following"]}}
    post_list = list(db_posts.find(following_query))
    for post in post_list:
        PostModel.format_date_data(post)
        user_data = db_users.find_one({"username": post["username"]})
        post["picture"] = user_data["picture"]
    post_dict["following"] = post_list[::-1]

    return json_util.dumps(post_dict)


# get user posts
@bp_routes.route("/posts/<user>", methods=["GET"])
def user_posts(user):
    cursor = list(db_posts.find({"username": user}))
    for post in cursor:
        user_data = db_users.find_one({"username": user})
        PostModel.format_date_data(post)
        post["picture"] = user_data["picture"]
        
    return json_util.dumps(cursor[::-1])


# get chapter by id
@bp_routes.route("/chapter/<chapterId>", methods=["GET"])
def chapter(chapterId):

    # search for chapter data
    chapter_query = {"_id": ObjectId(chapterId)}
    chapter_data = db_chapters.find_one(chapter_query)

    # find story prologue
    chapter_list = []
    story_query = {"_id": chapter_data["story_id"]}
    prologue_data = db_posts.find_one(story_query)
    user_query = {"username": prologue_data["username"]}
    user_data = db_users.find_one(user_query)
    prologue_data["picture"] = user_data["picture"]
    PostModel.format_date_data(prologue_data)

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
    
    # add prologue to first position
    chapter_list.insert(0, prologue_data)
    pprint(chapter_list)
    print(len(chapter_list))
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

    post_data["replies"] = replies
    pprint(post_data)
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
        "story_id": data.storyId,
        "username": data.username,
        "chapter_name": data.title,
        "chapter_num": data.chapterNum,
        "parent_chapter": data.parentChapterId,
        "content": data.body,
        "comment": data.comment
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


# edit posts
@bp_routes.route('/posts_edit', methods=["GET"])
@jwt_required()
def posts_edit():
    cursor = list(db_posts.find())
    for post in cursor:
        query = {"_id": post["_id"]}
        post["type"] = "prologue"

        db_posts.replace_one(query, post)
        
    return "Success"


# edit posts
@bp_routes.route('/comments_edit', methods=["GET"])
@jwt_required()
def comments_edit():
    comment_list = list(db_comments.find())
    for comment in comment_list:
        query = {"_id": comment["_id"]}

        comment["type"] = "comment"

        db_comments.replace_one(query, comment)
        
    return "Success"


# edit users
@bp_routes.route('/users_edit', methods=["GET"])
@jwt_required()
def users_edit():
    cursor = list(db_users.find())
    for user in cursor:
        #deleted = post.pop("pic_path", "not found")
        query = {"username": user["username"]}
        if user.get("followers") == None:
            user["followers"] = []
        if user.get("following") == None:
            user["following"] = []
        db_users.replace_one(query, user)
        
    return "successful change"


# edit users
@bp_routes.route('/chapters_edit', methods=["GET"])
def chapters_edit():
    
    chapter_list = list(db_chapters.find())

    for chapter in chapter_list:
        chapter_query = {"_id": chapter["_id"]}
        story_query = {"_id": chapter["story_id"]}
        story_data = db_posts.find_one(story_query)
        chapter["story_title"] = story_data["title"]
        db_chapters.replace_one(chapter_query, chapter)

    return "successful change"