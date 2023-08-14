from main import db_users, db_posts, db_comments, db_chapters
from werkzeug.security import check_password_hash
from bson.objectid import ObjectId
from config import COLOR_LIST, IMAGE_LIST
from typing import Dict, List
import datetime, random, math

class PostModel:
    def __init__(self, username, content, comment, title, tags, user_comments=None, leaves=None, color=None, status=None, 
                views=None, chapters=None, _id=None, date=None) -> None:
        self._id = ObjectId(_id) if _id else ObjectId()
        self.username = username
        self.date = date or datetime.datetime.now().isoformat()
        self.status = status or "active"
        self.title = title
        self.content = content
        self.comment = comment
        self.user_comments = user_comments or []
        self.color = color or random.choice(COLOR_LIST)
        self.views = views or 1
        self.chapters = chapters or {}
        self.type = "prologue"
        self.tags = tags or []
        self.leaves = leaves or []
        self.increase_num_started_stories()

    def quicksave_to_db(self):
        db_posts.insert_one(self.__dict__)

    def add_html_line_jumps(self):
        self.content = self.content.replace("\n", "<br>")

    def replace_db_doc(self):
        post_dict = self.__dict__
        db_posts.update_one({'_id': self._id}, {'$set': post_dict})

    def increase_num_started_stories(self):
        UserModel.update_started_story_count(self.username)

    def increase_visits(post_id):
        db_posts.update_one({'_id': post_id}, {'$inc': {'views': 1}})

    @staticmethod
    def format_date_data(post_data):
        t = datetime.datetime.fromisoformat(post_data["date"])
        now = datetime.datetime.now()
        dt = now - t
        minutes = int(dt.total_seconds() // 60)
        hours = int(minutes // 60)
        days = int(dt.days)
        if minutes < 2:
            formatted_date = f"Now" 
        elif hours < 1:
            formatted_date = f"{minutes}min ago" 
        elif days < 1:
            formatted_date = f"{hours}h ago"
        elif days < 2:
            formatted_date = f"Yesterday"
        elif days < 30:
            formatted_date = f"{days} days ago"
        elif days < 365:
            formatted_date = f"{math.ceil(days/30)} months ago"
        else:
            formatted_date = f"{math.ceil(days/365)} years ago"
        post_data["date"] = formatted_date
        
        return post_data
    
    @staticmethod
    def increase_leaves(post_id, username):
        db_posts.update_one({'_id': ObjectId(post_id)},
                            {'$push': {'leaves': username}})
        
    @staticmethod
    def decrease_leaves(post_id, username):
        db_posts.update_one({"_id": ObjectId(post_id)},
                                {"$pull": {"leaves": username}})

    @staticmethod
    def add_comment_id(post_id, comment_id):
        db_posts.update_one({'_id': ObjectId(post_id)},
                            {'$push': {'user_comments': comment_id}})
        

class ChapterModel:
    def __init__(self, story_id, username, chapter_name, chapter_num, parent_chapter_id, content, comment, views=None, leaves=None, story_title=None, 
                 continued_stories=None, color=None, status=None, date=None, tags=None, _id=None):
        self._id = ObjectId(_id) if _id else ObjectId()
        self.story_id = story_id
        self.parent_chapter_id = parent_chapter_id
        self.username = username
        self.date = date or datetime.datetime.now().isoformat()
        self.story_title = story_title or self.get_story_title()
        self.status = status or "active"
        self.chapter_name = chapter_name
        self.chapter_num = chapter_num
        self.content = content
        self.comment = comment
        self.continued_stories = continued_stories or []
        self.color = color or random.choice(COLOR_LIST)
        self.type = "chapter"
        self.leaves = leaves or []
        self.views = views or 0
        self.tags = tags or []
        self.increase_num_started_stories()
    
    def quicksave_to_db(self):
        db_chapters.insert_one(self.__dict__)
    
    def get_story_title(self):
        query = {"_id": self.story_id}
        story_data = db_posts.find_one(query)
        return story_data.get("title")
    
    def increase_num_started_stories(self):
        UserModel.update_continued_story_count(self.username)

    @staticmethod
    def increase_leaves(chapter_id, username):
        db_chapters.update_one({'_id': ObjectId(chapter_id)},
                                {'$push': {'leaves': username}})
    
    @staticmethod
    def decrease_leaves(chapter_id, username):
        db_chapters.update_one({"_id": ObjectId(chapter_id)},
                                {"$pull": {"leaves": username}})
    
    @staticmethod
    def increase_visits(chapter_id):
        db_chapters.update_one({'_id': ObjectId(chapter_id)}, 
                               {'$inc': {'views': 1}})