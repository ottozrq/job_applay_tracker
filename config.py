from flask import Flask

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
try:
    app.config.from_pyfile('config.py')
except:
    print('Missing instance/config.py, please create it manually.')
