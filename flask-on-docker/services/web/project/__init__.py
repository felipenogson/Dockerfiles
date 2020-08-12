import logging
from flask import Flask, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email


@app.route("/")
def index():
    """ Default route """
    app.logger.debug('this is a DEBUG message')
    app.logger.info('this is a INFO  message')
    app.logger.warning('this is a WARNING message')
    app.logger.error('this is a ERROR message')
    app.logger.critical('this is a CRITICAL message')
    return jsonify(hola="mundo", test="almost alive")


@app.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory(app.config['STATIC_FOLDER'], filename)
