class Game:
    
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
       
     

