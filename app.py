from flask import render_template, request, redirect, url_for
from flask_user import UserManager, login_required, current_user

from config import app
from scrapper import LinkedinScrapper
from model import db, User, Job
import jobs

user_manager = UserManager(app, db, User)


@app.route('/')
def index():
    if current_user.is_authenticated:
        username = current_user.username
        user_jobs = Job.objects(user_name=username)
        result = dict()
        result['jobs'] = [_serialize(a) for a in user_jobs]
        return render_template('index.html', result=result)
    return render_template('index.html')


@app.route('/jobs/add', methods=['POST'])
@login_required
def add_job():
    url = request.form['url']
    ls = LinkedinScrapper()
    result = ls.parse(url)
    jobs.add_new_job(result)
    return redirect(url_for('index'))


def _serialize(job):
    print(job)
    return {
        'title': job.title,
        'company': job.company,
        'location': job.location,
        'publish_date': job.publish_date,
        'apply_date': job.apply_date,
        'content': job.content,
        'replayed': job.replayed,
        'called': job.called,
        'tested': job.tested,
        'interviewed': job.interviewed,
        'rejected': job.rejected,
        'user_name': job.user_name,
    }


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
