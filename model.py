from flask_mongoengine import MongoEngine
from flask_user import UserMixin

from config import app

db = MongoEngine(app)


class User(db.Document, UserMixin):
    active = db.BooleanField(default=True)

    # User authentication information
    username = db.StringField(default='', unique=True)
    password = db.StringField()

    # User information
    first_name = db.StringField(default='')
    last_name = db.StringField(default='')


class Job(db.Document):
    title = db.StringField(default='')
    company = db.StringField(default='')
    location = db.StringField(default='')
    publish_date = db.DateTimeField()
    content = db.StringField(default='')
    user_id = db.StringField(default='')




