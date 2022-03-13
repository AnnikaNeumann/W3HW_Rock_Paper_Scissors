class Game:
    
    # when creating a class, you do not always need an init function if you are not storing variables for later, 
    # you are able to just have helper functions do the logic you need, making sure to pass all the data/variables you need into the function

    def let_the_games_begin(p1,p2):
        if p1.choice == p2.choice:
            return "It's a draw"

        elif p1.choice == "paper" and p2.choice == "rock":
            return f"{p1.name} won"

        elif p1.choice == "paper" and p2.choice == "scissors":
            return f"{p2.name} won"

        elif p1.choice == "rock" and p2.choice == "scissors":
            return f"{p1.name} won"
        
        elif p1.choice == "rock" and p2.choice == "paper":
            return f"{p2.name} won"
                
        elif p1.choice == "scissors" and p2.choice == "rock":
            return f"{p2.name} won"
        
        elif p1.choice == "scissors" and p2.choice == "paper":
            return f"{p1.name} won"
       
     

