from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from config import MONGODB_URI, SECRET_KEY, ALLOWED_ORIGIN
from flask_jwt_extended import JWTManager

# instantiate the app
app = Flask(__name__)
app.secret_key = SECRET_KEY

# enable CORS
CORS(app, resources={r'/*': {'origins': ALLOWED_ORIGIN}})

# instiantiate JSON Web Token authentication
jwt = JWTManager(app)

# pymongo config
app.config["MONGO_URI"] = MONGODB_URI
mongo = PyMongo(app)

# create collection instances
db_users = mongo.db.users
db_posts = mongo.db.posts
db_comments = mongo.db.comments
db_chapters = mongo.db.chapters
db_chapters2 = mongo.db.chapters2
db_stories = mongo.db.stories

# register blueprints
from routes.posts import bp_posts
app.register_blueprint(bp_posts)

from routes.users import bp_users
app.register_blueprint(bp_users)

from routes.edits import bp_edits
app.register_blueprint(bp_edits)