import datetime
from flask_user import current_user

from model import Job


def get_jobs(username):
    return Job.objects(user_name=username).order_by('-apply_date')


def add_new_job(json):
    url = json['url']
    title = json['title']
    company = json['company']
    location = json['location']
    publish_date = json['publish_date']
    apply_date = datetime.datetime.now()
    content = str(json['content'])
    user_name = current_user.username
    job = Job(url=url, title=title, company=company, location=location, publish_date=publish_date, apply_date=apply_date,
              content=content, user_name=user_name)
    job.save()


def delete_job(jid):
    job = Job.objects.get(id=jid)
    job.delete()


def job_rejected(jid):
    job = Job.objects.get(id=jid)
    job.update(rejected=True)
    job.save()


def job_update_status(jid, status):
    job = Job.objects.get(id=jid)
    if status == 'replayed':
        job.update(replayed=True)
    elif status == 'called':
        job.update(called=True)
    elif status == 'tested':
        job.update(tested=True)
    elif status == 'interviewed':
        job.update(interviewed=True)
    elif status == 'accepted':
        job.update(accepted=True)
    job.save()
