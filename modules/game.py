class Game:
    
    # when creating a class, you do not always need an init function if you are not storing variables for later, 
    # you are able to just have helper functions do the logic you need, making sure to pass all the data/variables you need into the function

    def let_the_games_begin(p1_choice,p2_choice):
        if p1_choice == p2_choice:
            return "It's a draw"

        elif p1_choice == "paper" and p2_choice == "rock":
            return "Player 1 wins"

        elif p1_choice == "paper" and p2_choice == "scissors":
            return "Player 2 win"

        elif p1_choice == "rock" and p2_choice == "scissors":
            return "Player 1 win"
        
        elif p1_choice == "rock" and p2_choice == "paper":
            return "Player 2 win"
                
        elif p1_choice == "scissors" and p2_choice == "rock":
            return "Player 2 wins"
        
        elif p1_choice == "scissors" and p2_choice == "paper":
            return "Player 1 wins"
       
     

