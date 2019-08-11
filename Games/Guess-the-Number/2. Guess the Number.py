import math
import random
import simplegui

secret_number = 0
n = 0
rang = 100

def new_game():
    global secret_number, n, rang
    secret_number = random.randrange(0,rang)

    if rang == 100:
        n = 7
    elif rang == 1000:
        n = 10
    else:
        return none
    
    print "\n"
    print "Welcome to \'Guess the number\'"
    print "The number you need to guess is between 0 and",rang
    print "You have",n,"attempts left."
    
def range100():
    global rang
    rang = 100
    new_game()
    
def range1000():
    global rang
    rang = 1000
    new_game()
    
def count():
    global n
    n -= 1
    return n
    
def input_guess(guess):
    guess = int(guess)
    print "Guess was",guess
    
    if guess < secret_number:
        print "Higher"
        print "You have", count(),"attempts left."
    elif guess > secret_number:
        print "Lower"
        print "You have", count(),"attempts left."
    else:
        print "YOU HAVE GUESSED IT RIGHT!"
        new_game()
    
    if n == 0:
        print "GAME OVER! Computer's guess was", secret_number
        new_game()
        
frame = simplegui.create_frame("Guess the number",200,200)
frame.add_label("Select appropriate range")
frame.add_button("Range: 0 - 100",range100)
frame.add_button("Range: 0 - 1000",range1000)
frame.add_input("Guess a number",input_guess,100)

new_game()
frame.start()
