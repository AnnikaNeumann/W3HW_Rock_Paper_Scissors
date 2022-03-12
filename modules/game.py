class Game:
    def __init__(self, p1, p2):
        self.p1_choice =  p1
        self.p2_choice = p2

# add choices of "rock", "paper" and "scissors"


    def let_the_games_begin(self):
        if self.p1_choice == self.p2_choice:
            return "It's a draw"

        elif self.p1_choice == "paper" and self.p2_choice == "rock":
            return "Paper wins"

        elif self.p1_choice == "paper" and self.p2_choice == "scissors":
            return "Scissors win"

        elif self.p1_choice == "scissors" and self.p2_choice == "rock":
            return "Rock wins"

        elif self.p1_choice == "rock" and self.p2_choice == "rock":
            return "It's a draw"

        if self.p1_choice == "scissors" and self.p2_choice == "scissors":
            return "It's a draw"

        if self.p1_choice == self.p2_choice:
            return "None"



        

