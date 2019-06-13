# implementation of card game - Memory

import simplegui
import random
# helper function to initialize globals
card_list = range(8) * 2
def new_game():
    global card_list, state, turns, exposed
    state = 0
    turns = 0
    random.shuffle(card_list)
    exposed = [False] * 16
    label.set_text("Turns = " + str(turns))
    
# define event handlers
def mouseclick(pos):
    global turns, state, exposed, pos1, pos2, card_list
    
    if state == 0:
        pos1 = pos[0] // 50
        if not exposed[pos1]:
            exposed[pos1] = True
            state = 1
        
    if state == 1:
        pos2 = pos[0] // 50
        if not exposed[pos2]:
            exposed[pos2] = True
            state = 2
            turns += 1
            label.set_text("Turns = " + str(turns))
           
    if state == 2:
         if not exposed[pos[0] // 50]:
                if (card_list[pos1] == card_list[pos2]):
                    pos1 = pos[0] // 50
                    exposed[pos1] = True
                    state = 1
                else:
                    exposed[pos1] = False
                    exposed[pos2] = False
                    pos1 = pos[0] // 50
                    exposed[pos1] = True
                    state = 1
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
   
    for card in range(16):   
        canvas.draw_text(str(card_list[card]), (card * 50 + 10, 60), 50, 'White')    
                    
        if not exposed[card]:
            canvas.draw_line((card * 50 + 25, 100), (card * 50 + 25, 0), 49,'Green')           

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric