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
    url = db.StringField(default='')
    title = db.StringField(default='')
    company = db.StringField(default='')
    location = db.StringField(default='')
    publish_date = db.StringField(default='')
    apply_date = db.DateTimeField()
    content = db.StringField(default='')
    replayed = db.BooleanField(default=False)
    called = db.BooleanField(default=False)
    tested = db.BooleanField(default=False)
    interviewed = db.BooleanField(default=False)
    accepted = db.BooleanField(default=False)
    rejected = db.BooleanField(default=False)
    user_name = db.StringField(default='')

    def serialize(self):
        status = '';
        if self.rejected:
            status = 'rejected'
            btn = ' - '
        elif self.accepted:
            status = 'accepted'
            btn = ' - '
        elif self.interviewed:
            status = 'interviewed'
            btn = 'accepted'
        elif self.tested:
            status = 'tested'
            btn = 'interviewed'
        elif self.called:
            status = 'called'
            btn = 'tested'
        elif self.replayed:
            status = 'replayed'
            btn = 'called'
        else:
            status = ' - '
            btn = 'replayed'
        return {
            'id': self.id,
            'url': self.url,
            'title': self.title,
            'company': self.company,
            'location': self.location,
            'publish_date': self.publish_date,
            'apply_date': self.apply_date,
            'content': self.content,
            'status': status,
            'btn': btn,
        }


