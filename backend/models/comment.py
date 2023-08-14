from main import db_users, db_posts, db_comments, db_chapters
from bson.objectid import ObjectId
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
    def add_to_parent(parent_id, comment):
        post_query = {"_id": ObjectId(parent_id)}
        db_posts.update_one(post_query, {"$addToSet": {"user_comments": ObjectId(comment["_id"])}})

    @staticmethod
    def find_docs_in_db(id_list):
        comments_list = []
        for _id in id_list:
            comments_list.append(db_comments.find_one({"_id": ObjectId(_id)}))

        return comments_list
    
    @staticmethod
    def add_pic_to_comments(comments):
        for comment in comments:
            username = comment["username"]
            user_data = db_users.find_one({"username": username})
            pic_path = user_data["pic_path"]
            comment["pic_path"] = pic_path
        
        return comments