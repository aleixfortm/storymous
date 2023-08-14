from main import db_stories
from bson.objectid import ObjectId
from typing import Dict, List
import datetime, random, math

class Story:
    def __init__(self, comments=None, chapters=None, _id=None, created_at=None) -> None:
        self._id = self._id = ObjectId(_id) if _id else ObjectId()
        self.created_at = created_at or datetime.datetime.now().isoformat()
        self.chapters = chapters or []
        self.comments = comments or []

    def save_to_db(self) -> str:
        result = db_stories.insert_one(self.__dict__)
        inserted_id = str(result.inserted_id)
        return inserted_id

    @staticmethod
    def increase_visits(story_id: str) -> None:
        db_stories.update_one({'_id': ObjectId(story_id)}, {'$inc': {'views': 1}})
