from main import db_users, db_posts, db_comments, db_chapters
from werkzeug.security import check_password_hash
from bson.objectid import ObjectId
from config import COLOR_LIST, IMAGE_LIST
from typing import Dict, List
import datetime, random, math

class UserModel:
    def __init__(self, username, email, password_hash, continued_stories=None, leaves=None, started_stories=None, comments=None, _id=None, bio=None, color=None, picture=None, following=None, followers=None, creation_date=None) -> None:
        self._id = ObjectId(_id) if _id else ObjectId()
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.creation_date = creation_date or datetime.datetime.now().isoformat()
        self.picture = picture or random.choice(IMAGE_LIST)
        self.color = color or random.choice(COLOR_LIST)
        self.bio = bio or f"Yo! I'm {self.username} and I love Storymous! Follow me to stay up to date with my content :^)"
        self.following = following or []
        self.followers = followers or []
        self.started_stories = started_stories or 0
        self.continued_stories = continued_stories or 0
        self.comments = comments or 0
        self.leaves = leaves or 0

    def get_id(self) -> str:
        return self._id

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)
    
    def quicksave_to_db(self) -> None:
        db_users.insert_one(self.__dict__)

    def replace_user(self) -> None:
        db_users.replace_one({"_id": self._id}, self.__dict__)
        
    # retrieve user data by username
    @staticmethod
    def find_by_username(username: str) -> Dict:
        return db_users.find_one({'_id': username})

    # retrieve user data by email
    @staticmethod
    def find_by_email(email: str) -> Dict:
        return db_users.find_one({'email': email})

    @staticmethod
    def format_date_data(user_data: Dict) -> Dict:
        t = datetime.datetime.fromisoformat(user_data["creation_date"])
        formatted_date = t.strftime('%b %d, %Y')
        user_data["creation_date"] = formatted_date
        return user_data

    @staticmethod
    def add_follower(user_being_followed, user_follows) -> None:
        # updating user being followed
        filter_query = {"username": user_being_followed}
        update_operation = {'$addToSet': {"followers": user_follows}}
        db_users.update_one(filter_query, update_operation)
        # updating user that follows
        filter_query = {"username": user_follows}
        update_operation = {'$addToSet': {"following": user_being_followed}}
        db_users.update_one(filter_query, update_operation)

    @staticmethod
    def remove_follower(user_being_unfollowed, user_stops_following) -> None:
        # updating user being unfollowed
        filter_query = {"username": user_being_unfollowed}
        update_operation = {'$pull': {"followers": user_stops_following}}
        db_users.update_one(filter_query, update_operation)
        # updating user that stops following
        filter_query = {"username": user_stops_following}
        update_operation = {'$pull': {"following": user_being_unfollowed}}
        db_users.update_one(filter_query, update_operation)

    @staticmethod
    def update_post_count_general(username) -> None:
        user_query = {"username": username}
        n_posts = len(list(db_posts.find(user_query)))
        new_value = {"$set": {"started_stories": n_posts}}
        db_users.update_one(user_query, new_value)

    @staticmethod
    def update_started_story_count(username) -> None:
        user_query = {"username": username}
        db_users.update_one(user_query, {"$inc": {"started_stories": 1}})

    @staticmethod
    def update_continued_story_count(username) -> None:
        user_query = {"username": username}
        db_users.update_one(user_query, {"$inc": {"continued_stories": 1}})

    @staticmethod
    def increase_leaves(username):
        db_users.update_one({'username': username},
                            {'$inc': {'leaves': 1}})
    @staticmethod
    def decrease_leaves(username):
        db_users.update_one({'username': username},
                            {'$inc': {'leaves': -1}})