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
      send_game(request)
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

def send_game(request):
   my_dict = {} 
   games = []
   games.append(create_game(request))
   my_dict["data"] = games
   my_dict["email"] = request.form['email']
   print(json.dumps(my_dict))
   
def create_game(request):
   my_dict = {}
   my_dict["teams"] = request.form['teams']
   my_dict["home"] = request.form['home']
   my_dict["away"] = request.form['away']
   my_dict["date"] = request.form['date']
   return my_dict
   
   