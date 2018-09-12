# Rock-paper-scissors-lizard-Spock template

import random

#Helper functions
#Conversion of name to number
def name_to_number(name):
    
    if name== "rock":
        name=0
    elif name== "Spock":
        name=1
    elif name== "paper":
        name=2
    elif name== "lizard":
        name=3
    elif name== "scissors":
        name=4
    else:
        print "Invalid Selection!!"
    return name    

#Conversion of number to name
def number_to_name(number):
    
    if number==0:
        number= "Rock"
    elif number==1:
        number= "Spock"
    elif number==2:
        number= "Paper"
    elif number==3:
        number= "Lizard"
    elif number==4:
        number= "Scissors"
    else:
        print "Please enter the correct number."
    return number    
    
#Main Fundtion, Computing Rock-Paper-Scissors-Lizard-Spock
def rpsls(player_choice): 
    
    print ""
    print "Player chooses",player_choice
    
    choosen = name_to_number(player_choice)
    player_number= choosen
    
    
    comp_number= random.randrange(0,5)
    comp_choice= number_to_name(comp_number)
    
    print "Computer chooses",comp_choice
    
    compute_difference= (player_number-comp_number)% 5
    
    if (compute_difference < 3) and (compute_difference>0):
        print "Player Wins!"
    elif compute_difference >= 3:
        print "Computer Wins!"
    elif compute_difference == 0:
        print "Player and Computer tie!"
    else:
        print "Methodological Error!!"
        
        
# Function Call 
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")