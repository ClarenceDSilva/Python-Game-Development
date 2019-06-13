# template for "Stopwatch: The Game"
import simplegui

# define global variables
current_time = "0:00.0"
score = "0/0"
minutes = 0
seconds = 0
milliseconds = 0
scr = 0
attempt = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global current_time
    global seconds
    global minutes
    
    if t < 600:
        seconds = t // 10
        milliseconds = t % 10
        minutes = 0
    elif (t > 599) and (t < 5999):
        minutes = (t // 600)
        s = t - (minutes * 600)
        milliseconds = (s % 10)
        seconds = (s // 10)
    
    if seconds <= 9:
         current_time =  str(minutes) +":0"+str(seconds)+"."+str(milliseconds)
    else:    
       current_time =  str(minutes) +":"+str(seconds)+"."+str(milliseconds)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    global scr
    global attempt
    global score, seconds, milliseconds
    
    if timer.is_running() == True:
        timer.stop()
        attempt += 1
        if ((milliseconds % 10) == 0):
            scr += 1
    
    score = str(scr)+"/"+str(attempt)   

def reset():
    global current_time, score, milliseconds, attempt, scr
    if (timer.is_running() == True) or (timer.is_running() == False):
        timer.stop()
        milliseconds = 0
        scr = 0
        attempt = 0
    score = str(scr)+"/"+str(attempt)
    format(milliseconds)
    milliseconds += 1
    
# define event handler for timer with 0.1 sec interval
def milli():
    global milliseconds
    
    milliseconds = milliseconds + 1
    
    
    #print milliseconds
    format(milliseconds)
   
# define draw handler
def curr_time(canvas):
     canvas.draw_text(str(current_time), (100, 150), 30, 'White')
     canvas.draw_text(str(score), (250,35), 30, 'Green')  
    
# create frame
frame = simplegui.create_frame("Stopwatch Game", 300 ,300)
frame.set_draw_handler(curr_time)
button1 = frame.add_button('Start', start, 50)
button2 = frame.add_button('Stop', stop, 50)
button3 = frame.add_button('Reset', reset, 50)



# register event handlers
timer = simplegui.create_timer(100, milli)


# start frame
frame.start()

# Please remember to review the grading rubric
