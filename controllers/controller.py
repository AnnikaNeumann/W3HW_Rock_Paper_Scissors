
from app import app 
from flask import render_template
from modules.game import *
from modules.player import *


# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/game_start')
# def make_choices():
#     return render_template('game_start.html')

@app.route('/<player_one>/<player_two>')
# the above variables refer to the choice of each player which we use in the url
# the above route takes in two variables, these two variables are being passed into the function, 
# the Function below MUST accept these variables, else it will error out, so two variables from browser means you need two into the function
def start_of_game(player_one,player_two):   

    # these variables below are used to play the game and comes directly from the browser input
    # below are two instances of the class Player, which contains the player's name and their choice
    player1 = Player("Jamie", player_one)
    player2 = Player("Claire", player_two)
    # the below variable game is a function from the class game, which is then used to run the actual game, passing in the two player choices
    # game = Game(player1,player2)
    result = Game.let_the_games_begin(player1,player2)
    
    # the variables passed into the render_template becomes available on the webpage refered to in the single quotes, 
    return render_template('index.html',player1web = player1, player2web = player2, result = result)


@app.route('/rules')
def rules():
    return render_template('rules.html')
     
    