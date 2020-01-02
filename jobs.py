import datetime
from flask_user import current_user

from model import Job


def add_new_job(json):
    title = json['title']
    company = json['company']
    location = json['location']
    publish_date = json['publish_date']
    apply_date = datetime.datetime.now()
    content = str(json['content'])
    user_name = current_user.username
    job = Job(title=title, company=company, location=location, publish_date=publish_date, apply_date=apply_date,
              content=content, user_name=user_name)
    job.save()
