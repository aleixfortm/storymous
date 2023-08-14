from flask import jsonify, request
from bson import json_util
from flask_pymongo import ObjectId
from flask import Blueprint, jsonify
from main import db_posts, db_users, db_comments, db_chapters
from models.models import PostModel, UserModel, CommentModel, ChapterModel
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from werkzeug.security import check_password_hash, generate_password_hash
from pprint import pprint


# create blueprint
bp_edits = Blueprint('edits', __name__)

"""
from collections import Counter
# edit posts
@bp_edits.route('/edit_stuff', methods=["GET"])
def posts_edit():
    user_counter = Counter()
    
    chapters = list(db_chapters.find())
    for chapter in chapters:
        user_counter[chapter["username"]] += 1
    
    pprint(user_counter)
    user_dict = dict(user_counter)
    for user, chapter_count in user_dict.items():
        query = {"username": user}
        update_data = {"$set": {"continued_stories": chapter_count}}
        db_users.update_one(query, update_data)
        

    chapters = list(db_chapters.find())
    for chapter in chapters:
        user_counter[chapter["username"]] += len(chapter["leaves"])

    user_dict = dict(user_counter)
    for user, leaves_count in user_counter.items():
        query = {"username": user}
        update_data = {"$set": {"leaves": leaves_count}}
        db_users.update_one(query, update_data)

        
    return "Success"


# edit posts
@bp_edits.route('/edit_stuff', methods=["GET"])
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

"""