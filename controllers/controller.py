
from app import app 
from flask import render_template
from modules.game import *
from modules.player import *


# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/<player_one>/<player_two>')
# the above route takes in two variables, these two variables are being passed into the function, 
# the Function below MUST accept these variables, else it will error out, so two variables from browser means you need two into the function
def start_of_game(player_one,player_two):   

    # these variables below are used to play the game and comes directly from the browser input
    player1 = player_one
    player2 = player_two
    # the below variable game is a function from the class game, which is then used to run the actual game, passing in the two player choices
    # game = Game(player1,player2)
    result = Game.let_the_games_begin(player1,player2)
    
    # the variables passed into the render_template becomes available on the webpage refered to in the single quotes, 
    return render_template('index.html',player1Choice = player1, player2Choice = player2, result = result)


# @app.route('/result')
# def let_the_games_begin():


#     return render_template('rock_paper_scissors.html', rock_paper_scissors = "Testing stuff", title='Home')


# @app.route('/choice_p1, choice_p2')
# def let_the_games_begin(p1, p2):
