from main import db_stories
from bson.objectid import ObjectId
from typing import Dict, List
import datetime, random, math

class Story:
    def __init__(self, leaves=1, comments=None, views=None, chapters=None, _id=None, created_at=None) -> None:
        self._id = self._id = ObjectId(_id) if _id else ObjectId()
        self.created_at = created_at or datetime.datetime.now().isoformat()
        self.chapters = chapters or []
        self.comments = comments or []
        self.views = views or 1

    def save_to_db(self) -> None:
        db_stories.insert_one(self.__dict__)

    @staticmethod
    def increase_visits(story_id: str) -> None:
        db_stories.update_one({'_id': ObjectId(story_id)}, {'$inc': {'views': 1}})
