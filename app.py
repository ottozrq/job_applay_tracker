from flask import render_template
from flask_user import UserManager, login_required

from config import app
from scrapper import LinkedinScrapper
from model import db, User

user_manager = UserManager(app, db, User)


@app.route('/')
def home_page():
    return render_template('index.html')





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
