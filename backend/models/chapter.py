from main import db_chapters2
from models.user import User
from bson.objectid import ObjectId
import datetime, random, math

class Chapter:
    def __init__(self, username, content, story_id, chapter_num, comment, title, parent_id, tags, leaves=None, status=None, 
                views=None, _id=None, created_at=None) -> None:
        self._id = ObjectId(_id) if _id else ObjectId()
        self.story_id = ObjectId(story_id)
        self.parent_id = ObjectId(parent_id) or None
        self.username = username
        self.created_at = created_at or datetime.datetime.now().isoformat()
        self.status = status or "active"
        self.title = title
        self.content = content
        self.comment = comment
        self.views = views or 1
        self.chapter_num = chapter_num
        self.tags = tags or []
        self.leaves = leaves or [username]
    
    def increase_user_written_stories(self) -> None:
        if self.chapter_num == 0:
            User.update_started_story_count(self.username)
        else:
            User.update_continued_story_count(self.username)
    
    def save_to_db(self) -> None:
        db_chapters2.insert_one(self.__dict__)
    
    @staticmethod
    def increase_visits(chapter_id) -> None:
        db_chapters2.update_one({'_id': ObjectId(chapter_id)}, {'$inc': {'views': 1}})
    
    @staticmethod
    def format_date_data(date: str) -> str:
        t = datetime.datetime.fromisoformat(date)
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
        
        return formatted_date
    
    @staticmethod
    def increase_leaves(chapter_id, username):
        db_chapters2.update_one({'_id': ObjectId(chapter_id)},
                            {'$push': {'leaves': username}})
        
    @staticmethod
    def decrease_leaves(chapter_id, username):
        db_chapters2.update_one({"_id": ObjectId(chapter_id)},
                                {"$pull": {"leaves": username}})