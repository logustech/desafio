from flask import Blueprint, Flask, render_template, request
from flaskext.mysql import MySQL
from app.database import Database
import requests
import json

db = Database()
bp_app = Blueprint("home", __name__)

@bp_app.route("/")
def index():
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
   send_dict = {} 
   games = []
   games.append(create_game(request))
   send_dict["data"] = games
   send_dict["email"] = request.form['email']
   game_json = json.dumps(send_dict)
   url = 'http://desafio.logus.tech/desafio'
   requests.post(url, data = game_json)
   
def create_game(request):
   game_dict = {}
   game_dict["id"] = request.form['game_id']
   game_dict["teams"] = request.form['teams']
   game_dict["home"] = request.form['home']
   game_dict["away"] = request.form['away']
   game_dict["date"] = request.form['date']
   return game_dict
   
   