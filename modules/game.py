class Game:
    def __init__(self, choice_1, choice_2):
        self.choice_1 =  choice_1
        self.choice_2 = choice_2

# add choices of "rock", "paper" and "scissors"
    choice =("rock", "paper", "scissor")


    def let_the_games_begin(self, choice_1, choice_2):
        if choice_1 == choice_2:
            return "It's a draw"

        if choice_1 == "paper" + choice_2 == "rock":
            return "Rock wins"

        if choice_1 == "scissors" + choice_2 == "paper":
            return "Scissors win"

      


