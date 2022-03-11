from app import app 
from flask import render_template
from modules.game import *
from modules.player import *

@app.route('/rock_paper_scissors')
def welcome():
    return render_template('index.html', title='Home', position= "Player 1 :It's your turn")


