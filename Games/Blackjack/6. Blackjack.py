# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
message_player = ""
message = ""
score = 0
player_hand = []
dealer_hand = []
deck_list = []
new_deck = []
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand_object = []
        
    def __str__(self):
        s = ""
        for i in range(len(self.hand_object)):
            s += str(self.hand_object[i]) + " " 
        string = "Hand Contains "+ s    
        return string
                
    def add_card(self, card):
        self.hand_object.append(card)
        return self.hand_object

    def get_value(self):
        hand_value = 0
        
        for i in self.hand_object:
            rank = i.get_rank()
            hand_value += VALUES.get(rank)
        
        for i in self.hand_object:
            rank = i.get_rank()
            if rank != 'A':
                return hand_value
            elif rank == 'A' and hand_value <= 21:
                return hand_value + 10
            else:
                return hand_value
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
                

    def draw(self, canvas, pos):
        for card in self.hand_object:
            card.draw(canvas, pos)
            pos[0] += 100
        if in_play == True:
            # Draw the back-card image on top of the 1st card of dealer_hand
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [116,183], CARD_BACK_SIZE)
     
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck_list = []
        self.deal_card()
        self.shuffle()
    
    def shuffle(self):
        return random.shuffle(self.deck_list)

    def deal_card(self):
        while(len(self.deck_list)<=52):
            for x in SUITS:
                for y in RANKS:
                    self.new_card = Card(str(x), str(y)) 
                    self.deck_list.append(self.new_card)
                                              
        s = self.deck_list.pop(-1)
        return s      
    
    def __str__(self):
        
        st = ""
        for i in range(len(self.deck_list)):
            st += str(self.deck_list[i])+ " "
        string = "Deck Contains:" + st
        return string


#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, new_deck, message_player, message,score
    
    if in_play == True:
        outcome = "Round forfeited, You lose!"
        message_player = "New deal in progress"
        score -= 1
        new_deck = Deck() # will automatically produce a new deck of cards shuffled   
        player_hand = Hand()
        dealer_hand = Hand()
        player_hand.add_card(new_deck.deal_card())
        dealer_hand.add_card(new_deck.deal_card())
        player_hand.add_card(new_deck.deal_card())
        dealer_hand.add_card(new_deck.deal_card())        
    
    if in_play == False:
        new_deck = Deck() # will automatically produce a new deck of cards shuffled   
        player_hand = Hand()
        dealer_hand = Hand()
        player_hand.add_card(new_deck.deal_card())
        dealer_hand.add_card(new_deck.deal_card())
        player_hand.add_card(new_deck.deal_card())
        dealer_hand.add_card(new_deck.deal_card())
        outcome = ""
    in_play = True    
    

def hit():
    global outcome, in_play, player_hand, dealer_hand, new_deck, score, message_player, message
    
    if in_play == True:
        player_hand.add_card(new_deck.deal_card())
        message_player = "Hit or Stand?"        
        if player_hand.get_value() > 21:
            outcome = "You went bust and lost!"
            message_player = "New Deal?"
            score -= 1
            in_play = False     
    
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome, in_play, player_hand, dealer_hand, new_deck, score, message_player, message
    
    
    while dealer_hand.get_value() <= 17:
        dealer_hand.add_card(new_deck.deal_card())
    if dealer_hand.get_value() > 21:
        outcome = "Dealer Busted, You win!"
        message_player = "New Deal?"
        score += 1
        in_play = False
    elif dealer_hand.get_value() == player_hand.get_value():
        outcome = "You went bust and lost"
        message_player = "New Deal?"
        score -= 1
        in_play = False
    elif dealer_hand.get_value() > player_hand.get_value():
        outcome = "You went bust and lost"
        message_player = "New Deal?"
        score-= 1
        in_play = False
    else:
        outcome = "Dealer Busted, You win!"
        message_player = "New Deal?"
        score += 1
        in_play = False        
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global outcome

    canvas.draw_text('Blackjack', (200,50), 45, 'Yellow')
    canvas.draw_text(outcome, (200,100), 25, 'Black')
    canvas.draw_text(message_player, (200,300), 25, 'Black')
    canvas.draw_text('Dealer:', (80,100), 25, 'Black')
    canvas.draw_text('Player:', (80,300), 25, 'Black')
    canvas.draw_text('Score:  ' +str(score), (450,55), 25, 'Black')
    dealer_hand.draw(canvas, [80,135])
    player_hand.draw(canvas, [80,325])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric