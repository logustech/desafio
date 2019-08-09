from flask import Blueprint, Flask, render_template, request
from flaskext.mysql import MySQL
from app.database import Database
import json

db = Database()
bp_app = Blueprint("home", __name__)

@bp_app.route("/")
@bp_app.route("/home")
def home():
   return render_index()

@bp_app.route("/edit", methods=['POST','GET'])
def edit():
   if request.method == 'POST':
      home=request.form['home']
      teams=request.form['teams']
      away=request.form['away']
      date=request.form['date']
      email=request.form['email']
      return render_index()
   else:
      game_id = request.args.get('game_id')
      game = db.find_game_by_id(game_id)
      return render_template('edit.html', game = game)

def configure(app):
   app.register_blueprint(bp_app)
   
def render_index():
   games = db.events_list()
   return render_template('index.html', result = games)