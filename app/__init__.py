from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from flaskext.mysql import MySQL
from app.blueprints import home

def create_app():
    app = Flask(__name__)
    home.configure(app)

    return app
