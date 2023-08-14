from main import db_comments, db_stories
from models.user import User
from bson.objectid import ObjectId
from typing import List
import datetime

class CommentModel:
    def __init__(self, username, comment, status=None, _id=None, date=None):
        self._id = ObjectId(_id) if _id else ObjectId()
        self.username = username
        self.status = status or "active"
        self.comment = comment
        self.date = date or datetime.datetime.now().isoformat()
        self.type = "comment"
    
    def quicksave_to_db(self):
        db_comments.insert_one(self.__dict__)
    
    @staticmethod
    def add_to_parent(story_id, comment_id):
        story_query = {"_id": ObjectId(story_id)}
        db_stories.update_one(story_query, {"$addToSet": {"comments": ObjectId(comment_id["_id"])}})
    
    @staticmethod
    def add_pic_to_comments(comments: List) -> List:
        for comment in comments:
            username = comment["username"]
            comment["pic_path"] = User.find_picture(username)
        
        return comments