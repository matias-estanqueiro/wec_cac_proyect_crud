from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .views import views
from .auth import auth

users = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '8f42a73054b1749f8f58848be5e6502c'

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app