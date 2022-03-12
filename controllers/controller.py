from random import *
from app import app 
from flask import render_template
from modules.game import *
from modules.player import *


@app.route('/rock_paper_scissors')
def welcome():
    return render_template('index.html', title='Home')

@app.route('/rock_paper_scissors', methods=['POST'])
def choose_item():
    new_turn = Player(request.form[''],request.form[""])
    choose_item(new_turn)
    return render_template('rock_paper_scissors.html', title="Rock-Paper-Scissors")
