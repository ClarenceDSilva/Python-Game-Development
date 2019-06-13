# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [-2, -1]
paddle1_pos = [150, 250]
paddle2_pos = [150, 250]
paddle1_vel = [0, 0]
paddle2_vel = [0, 0]
score1 = score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_vel[0] = random.randrange(3, 4)
    ball_vel[1] = random.randrange(3, 4)
     
    if direction == LEFT:
        ball_vel[0] = - ball_vel[0]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    if LEFT:
        spawn_ball(LEFT)
    elif RIGHT:
        spawn_ball(RIGHT)
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    #spawn_ball()    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # collide and reflect the top and bottom of the canvas
    if (ball_pos[1] <= BALL_RADIUS) or (ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    
    # conditions for colliding and reflecting the paddles and gutters 
    if ball_pos[0]  <= (BALL_RADIUS + PAD_WIDTH):
        if (ball_pos[1] >= paddle1_pos[0]) and (ball_pos[1] <= paddle1_pos[1]):
            ball_vel[0] = - ball_vel[0] * 1.1
            #ball_vel[0] += 2
        else:
            ball_vel[0] = - ball_vel[0]
            ball_vel = [2, -1]
            ball_pos = [300, 200]
            spawn_ball(RIGHT)
            score2 += 1
          
    if ball_pos[0] >= ((WIDTH - 1) - PAD_WIDTH - BALL_RADIUS):
        if (ball_pos[1] >= paddle2_pos[0]) and (ball_pos[1] <= paddle2_pos[1]):
            ball_vel[0] = - ball_vel[0] *1.1
            #ball_vel[1] += 1
        else:
            ball_vel[0] = - ball_vel[0]
            ball_vel = [-2, -1]
            ball_pos = [300, 200]
            score1 += 1
            spawn_ball(LEFT)
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] -= ball_vel[1]        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 3,'Green', 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[0] += paddle1_vel[0]
    paddle1_pos[1] += paddle1_vel[1]
    
    paddle2_pos[0] += paddle2_vel[0]
    paddle2_pos[1] += paddle2_vel[1]
    
    # boundary conditions for paddle 1 (***i missed out***)
    if (paddle1_pos[0] <= HEIGHT - 1) and (paddle1_pos[1] <= (HEIGHT - 1) -300):
        paddle1_vel[0] = 0
        paddle1_vel[1] = 0
        
    elif (paddle1_pos[1] >= (HEIGHT + 1)) and (paddle1_pos[0] >= ((HEIGHT + 1) - 100)):
        paddle1_vel[0] = 0
        paddle1_vel[1] = 0
        
    # boundary conditions for paddle 2
    elif (paddle2_pos[0] <= HEIGHT - 1) and (paddle2_pos[1] <= (HEIGHT - 1) -300):
        paddle2_vel[0] = 0
        paddle2_vel[1] = 0
        
    elif (paddle2_pos[1] >= (HEIGHT + 1)) and (paddle2_pos[0] >= ((HEIGHT + 1) - 100)):
        paddle2_vel[0] = 0
        paddle2_vel[1] = 0   
    
    # draw paddles
    canvas.draw_line([0, paddle1_pos[0]], [0, paddle1_pos[1]], (2 * PAD_WIDTH), "Aqua")
    canvas.draw_line([(WIDTH - 1), paddle2_pos[0]], [(WIDTH - 1), paddle2_pos[1]], (2 * PAD_WIDTH), "Aqua")
    
    # draw scores
    canvas.draw_text(str(score1), (150, 50), 35, 'White')
    canvas.draw_text(str(score2), (450, 50), 35, 'White')
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["S"]:
        paddle1_vel[0] +=8
        paddle1_vel[1] +=8
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[0] +=8
        paddle2_vel[1] +=8
        
    elif key == simplegui.KEY_MAP["W"]:
        paddle1_vel[0] -=8
        paddle1_vel[1] -=8
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel[0] -=8
        paddle2_vel[1] -=8       
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    paddle1_vel[0] =0
    paddle1_vel[1] =0
 
    paddle2_vel[0] =0
    paddle2_vel[1] =0 

def restart():
    global ball_pos, score1, score2
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    score1 = score2 =0
    score2 = 0   

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart, 100 )


# start frame
new_game()
frame.start()
