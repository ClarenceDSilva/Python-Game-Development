# "Guess the number" 
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

secret_number=0
your_guess=0
num_range = 100 

if your_guess < num_range:
    
    high = 99
    low = 0
    n = (math.log((high - low + 1), 10))/(math.log(2, 10))
    guesses = math.trunc(math.ceil(n))

# helper function to start and restart the game

def new_game():
    # initialize global variables used in your code here
    
    global secret_number
    secret_number = random.randrange(0,100)
    high = 99
    low = 0
    n = (math.log((high - low + 1), 10))/(math.log(2, 10))
    guesses = math.trunc(math.ceil(n))
    
    print "New Game, Range is from 0 to 100"
    print "Number of remaining guesses is",guesses
    
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    high = 99
    low = 0
    n = (math.log((high - low + 1), 10))/(math.log(2, 10))
    guesses = math.ceil(n)
   
    print "New Game, Range is from 0 to 100"
    print "Number of remaining guesses is",guesses
 
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global guesses
    global secret_number
    #global your_guess
    secret_number = random.randrange(0,1000)
    high = 999
    low = 0
    n = (math.log((high - low + 1), 10))/(math.log(2, 10))
    guesses = math.trunc(math.ceil(n))
    
    print "New Game, Range is from 0 to 1000"
    print "Number of remaining guesses is",guesses
        
def input_guess(guess):
    # main game logic goes here	
    global guesses
    global num_range
    global your_guess
    
    your_guess = int(guess)
    #range100()
    
    print ""
    print "Your guess was:",your_guess    
        
    if (your_guess < secret_number) and (guesses >= 3):
        print " Go Higher!"
        guesses = guesses - 1
        print "You have",guesses,"guesses remaining"
    
    elif (your_guess > secret_number) and (guesses >= 3):
        print "Go Lower!"
        guesses = guesses - 1
        print "You have",guesses,"guesses remaining"
        
    elif (your_guess < secret_number) and (guesses == 2):
        print " Go Higher!"
        guesses = guesses - 1
        print "This is your Final Guess!!"
    
    elif (your_guess > secret_number) and (guesses == 2):
        print "Go Lower!"
        guesses = guesses - 1
        print "This is your Final guess!!"    
    
    elif your_guess == secret_number:
        print "You Guessed it Right!!"
        new_game()
    
    else:
        print "Game Over!!"
        print "Sorry, you have no Guesses remaining "
        new_game()
   

    
# create frame
frame = simplegui.create_frame("Guess The Number!!",200,200)
frame.set_canvas_background('Black')
frame.start()

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Enter a Guess!!", input_guess, 200)

# call new_game 
new_game()
