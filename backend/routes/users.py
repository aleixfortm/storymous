from flask import jsonify, request
from bson import json_util
from flask_pymongo import ObjectId
from flask import Blueprint, jsonify
from main import db_posts, db_users, db_comments, db_chapters
from models.models import PostModel, UserModel, CommentModel, ChapterModel
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from werkzeug.security import check_password_hash, generate_password_hash
from pprint import pprint
from datetime import timedelta
import random

# create blueprint
bp_users = Blueprint('users', __name__)


# sign up sequence
@bp_users.route("/signup", methods=["POST"])
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
@bp_users.route('/login', methods=['POST'])
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
@bp_users.route("/user/<user>", methods=["GET"])
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
@bp_users.route("/settings/<user>", methods=["GET"])
def get_settings(user):
    user_data = db_users.find_one({"username": user})
    settings_data = {
        "color": user_data["color"],
        "bio": user_data["bio"],
        "picture": user_data["picture"]
    }

    return json_util.dumps(settings_data)

# follow updates
@bp_users.route('/follow', methods=['POST'])
@jwt_required()
def follow():
    data = request.json
    if data.get("action") == "follow":
        UserModel.add_follower(data.get("user_being_followed"), data.get("user_follows"))
        return json_util.dumps("Success")
    
    else:
        UserModel.remove_follower(data.get("user_being_followed"), data.get("user_follows"))
        return json_util.dumps("Success")
    

@bp_users.route("/update_settings", methods=["POST"])
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