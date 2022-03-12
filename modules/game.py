class Game:
    def __init__(self, p1, p2):
        self.choice_p1 =  p1
        self.choice_p2 = p2

# add choices of "rock", "paper" and "scissors"


    def let_the_games_begin(self):
        if self.choice_p1 == self.choice_p2:
            return "It's a draw"

        elif self.choice_p1 == "paper" and self.choice_p2 == "rock":
            return "Paper wins"

        elif self.choice_p1 == "paper" and self.choice_p2 == "scissors":
            return "Scissors win"

        elif self.choice_p1 == "scissors" and self.choice_p2 == "rock":
            return "Rock wins"

        elif self.choice_p1 == "rock" and self.choice_p2 == "rock":
            return "It's a draw"

        if self.choice_1p == "scissors" and self.choice_p2 == "scissors":
            return "It's a draw"

        if self.choice_p1 == self.choice_p2:
            return "It's a daw"



        

