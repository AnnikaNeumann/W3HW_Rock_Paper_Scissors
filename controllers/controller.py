
from app import app 
from flask import render_template, request
from modules.game import *
from modules.player import *


@app.route('/index.html')
def welcome():
    return render_template('index.html', title='Home')

@app.route('/choice_p1, choice_p2')
def let_the_games_begin(p1, p2):
    p1 = Player("Player 1", p1)
    p2 = Player("Player 2", p2)
    results = let_the_games_begin(p1, p2,)
    return render_template('index.html', title="Home", Player1 = p1, Player2 = p2, results = results)
