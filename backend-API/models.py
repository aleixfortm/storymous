from main import db_users, db_posts, db_comments, db_chapters
from werkzeug.security import check_password_hash
from bson.objectid import ObjectId
from config import COLOR_LIST, IMAGE_LIST
from typing import Dict, List
import datetime, random, math


class UserModel:
    def __init__(self, username, email, password_hash, continued_stories=None, started_stories=None, comments=None, _id=None, bio=None, color=None, picture=None, following=None, followers=None, creation_date=None) -> None:
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


class PostModel:
    def __init__(self, username, content, comment, title, user_comments=None, color=None, status=None, 
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

    def increase_visits(post_id, ):
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
        elif days > 30 and days < 365:
            formatted_date = f"{math.ceil(days/30)} months ago"
        else:
            formatted_date = f"{math.ceil(days/365)} years ago"
        post_data["date"] = formatted_date
        
        return post_data

    @staticmethod
    def add_comment_id(post_id, comment_id):
        db_posts.update_one({'_id': ObjectId(post_id)},
                            {'$push': {'user_comments': comment_id}})
        

class ChapterModel:
    def __init__(self, story_id, username, chapter_name, chapter_num, parent_chapter_id, content, comment, story_title=None, continued_stories=None, color=None, status=None, date=None, _id=None):
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
        self.increase_num_started_stories()
    
    def quicksave_to_db(self):
        db_chapters.insert_one(self.__dict__)

    def add_record_to_main_story(self):
        query = {"_id": self.story_id}
        db_posts.find_one()
    
    def get_story_title(self):
        query = {"_id": self.story_id}
        story_data = db_posts.find_one(query)
        return story_data.get("title")
    
    def increase_num_started_stories(self):
        UserModel.update_continued_story_count(self.username)

                    
class CommentModel:
    def __init__(self, username, comment, status=None, _id=None, date=None):
        self._id = ObjectId(_id) if _id else ObjectId()
        self.username = username
        self.status = status or "active"
        self.comment = comment
        self.date = date or datetime.datetime.now().isoformat()
        self.type = "comment"
    
    def quicksave_to_db(self):
        db_posts
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