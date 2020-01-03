from flask import render_template, request, redirect, url_for
from flask_user import UserManager, login_required, current_user

from config import app
from scrapper import LinkedinScrapper
from model import db, User
import jobs

user_manager = UserManager(app, db, User)


@app.route('/')
def index():
    if current_user.is_authenticated:
        username = current_user.username
        user_jobs = jobs.get_jobs(username)
        result = dict()
        result['jobs'] = [a.serialize() for a in user_jobs]
        return render_template('index.html', result=result, title='Applications')
    return render_template('index.html')


@app.route('/rejected')
def rejected():
    username = current_user.username
    user_jobs = jobs.get_jobs_rejected(username)
    result = dict()
    result['jobs'] = [a.serialize() for a in user_jobs]
    return render_template('index.html', result=result, title='Rejected')


@app.route('/replied')
def replied():
    username = current_user.username
    user_jobs = jobs.get_jobs_replied(username)
    result = dict()
    result['jobs'] = [a.serialize() for a in user_jobs]
    return render_template('index.html', result=result, title='Replied')


@app.route('/rien')
def rien():
    username = current_user.username
    user_jobs = jobs.get_jobs_rien(username)
    result = dict()
    result['jobs'] = [a.serialize() for a in user_jobs]
    return render_template('index.html', result=result, title='No Response')


@app.route('/jobs/add', methods=['POST'])
@login_required
def add_job():
    url = request.form['url']
    ls = LinkedinScrapper()
    result = ls.parse(url)
    jobs.add_new_job(result)
    return redirect(url_for('index'))


@app.route('/jobs/delete/<jid>', methods=['POST'])
@login_required
def delete_job(jid):
    jobs.delete_job(jid)
    return redirect(url_for('index'))


@app.route('/jobs/reject/<jid>', methods=['POST'])
@login_required
def reject(jid):
    jobs.job_rejected(jid)
    return redirect(url_for('index'))


@app.route('/jobs/update/<jid>/<status>', methods=['post'])
@login_required
def update(jid, status):
    jobs.job_update_status(jid, status)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
