import os
from flask import Flask
from board import pages, posts
pip install python-dotenv

from dotenv import load_dotenv
load_dotenv()

def create_app():
    app = Flask(__name__)

    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)
    return app
    app.register_blueprint(pages.bp)