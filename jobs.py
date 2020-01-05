import datetime
from flask_user import current_user

from model import Job


def get_jobs(username):
    return Job.objects(user_name=username).order_by('-apply_date')


def get_job_by_id(jid):
    return Job.objects.get(id=jid)


def get_jobs_rejected(username):
    return Job.objects(user_name=username, rejected=True).order_by('-apply_date')


def get_jobs_replied(username):
    return Job.objects(user_name=username, replayed=True).order_by('-apply_date')


def get_jobs_rien(username):
    return Job.objects(user_name=username, replayed=False, rejected=False).order_by('-apply_date')


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
    if status == 'replied':
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


def job_update_status_checkbox(jid, checkboxes):
    job = Job.objects.get(id=jid)
    if 'replied' in checkboxes:
        job.update(replayed=True)
    else:
        job.update(replayed=False)
    if 'called' in checkboxes:
        job.update(called=True)
    else:
        job.update(called=False)
    if 'tested' in checkboxes:
        job.update(tested=True)
    else:
        job.update(tested=False)
    if 'interviewed' in checkboxes:
        job.update(interviewed=True)
    else:
        job.update(interviewed=False)
    if 'accepted' in checkboxes:
        job.update(accepted=True)
    else:
        job.update(accepted=False)
    if 'rejected' in checkboxes:
        job.update(rejected=True)
    else:
        job.update(rejected=False)
    job.save()
