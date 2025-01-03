
import turtle
import winsound
import time
import random

wn = turtle.Screen()
wn.title("Pong by DuyMinh")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
# Score
score_a = 0
score_b = 0
winning_score = 10
# Add new variables for customization and control
paddle_color_a = 'red'
paddle_color_b = 'blue'
ball_color = 'white'
is_paused = False
sound_on = True

# Function to toggle pause
def toggle_pause():
    global is_paused
    is_paused = not is_paused

# Function to toggle sound
def toggle_sound():
    global sound_on
    sound_on = not sound_on

# Function to play sound with sound control
def play_sound(sound_file):
    if sound_on:
        winsound.PlaySound(sound_file, winsound.SND_ASYNC)

# Function to change paddle size
def increase_paddle_size(paddle):
    if paddle.shapesize()[1] < 10:  # Maximum size limit
        paddle.shapesize(stretch_wid=5, stretch_len=paddle.shapesize()[1] + 1)


# Help 
help = turtle.Turtle() 
help.speed(0)
help.color("cyan")
help.penup()
help.hideturtle()
help.goto(0,-240)
help.write("W S or Up Down : To Move ", align="center", font=("Courier", 13, "normal"))
help.goto(0,-260)
help.write("P: Pause    M : On/off Sound ", align="center", font=("Courier", 13, "normal"))
help.goto(0,-280)
help.write("1:Easy 2:Medium 3:Hard ", align="center", font=("Courier", 13, "normal"))


# Name Player 
NameA = turtle.textinput("Player A name:","What is your Name ?:")
play_sound("bounce.wav")
NameB = turtle.textinput("Player B name:","What is your Name ?:")
play_sound("bounce.wav")
Name = turtle.Turtle()
Name.speed(0)
Name.color("white")
Name.penup()
Name.hideturtle()
Name.goto(0, 200)
Name.write("Name A:      {}  Name B:       {}".format(NameA, NameB), align="center", font=("Courier", 20, "normal"))
# Game state flags
Game_Run = True
multi_ball_active = False
current_difficulty = '1'  # Default difficulty
current_difficulty = turtle.textinput("Difficulty","1:Easy 2:Medium 3:Hard")
# Difficulty settings
ball_speeds = {'1': 0.1, '2': 0.2, '3': 0.3}
# Power-up settings
power_up_active = False
power_up_timer = 0



# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(-350, 0)
ball.dx = ball_speeds[current_difficulty]
ball.dy = -ball_speeds[current_difficulty]

# Additional Ball for Multi-ball Feature
extra_ball = turtle.Turtle()
extra_ball.speed(0)
extra_ball.shape("square")
extra_ball.color("blue")
extra_ball.penup()
extra_ball.goto(0, 0)
extra_ball.dx = 0.15
extra_ball.dy = -0.15
extra_ball.hideturtle()

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score A: {}  score B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

# WIN
win = turtle.Turtle()
win.speed(0)
win.color("white")
win.penup()
win.hideturtle()
# Function to set difficulty
def set_difficulty(level):
    global ball_speeds
    current_difficulty = level
    ball.dx, ball.dy = ball_speeds[level], -ball_speeds[level]
    
set_difficulty(current_difficulty)


# Function to activate multi-ball
def activate_multi_ball():
    global multi_ball_active
    multi_ball_active = True
    extra_ball.showturtle()

# Function to deactivate multi-ball
def deactivate_multi_ball():
    global multi_ball_active
    multi_ball_active = False
    extra_ball.hideturtle()

# Function to activate a power-up
def activate_power_up():
    global power_up_active, power_up_timer
    power_up_active = True
    power_up_timer = time.time()

# Function to deactivate a power-up
def deactivate_power_up():
    global power_up_active
    power_up_active = False

# Paddle movement functions
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:  # Boundary check
        y += 70
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:  # Boundary check
        y -= 70
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:  # Boundary check
        y += 70
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:  # Boundary check
        y -= 70
        paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(toggle_pause, "p")
wn.onkeypress(toggle_sound, "m")
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(lambda: set_difficulty('1'), "1")
wn.onkeypress(lambda: set_difficulty('2'), "2")
wn.onkeypress(lambda: set_difficulty('3'), "3")




# Main game loop
def main_game_loop():
 global Game_Run
 global score_a
 global score_b
 while Game_Run:
  if not is_paused:
    wn.update()
    
    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        play_sound("bounce.wav")
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        play_sound("bounce.wav")
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(350, 0)
        ball.dx *= -1
        play_sound("score.wav")
        score_a += 1
        pen.clear()
        pen.write("Score A: {}  score B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(-350, 0)
        ball.dx *= -1
        play_sound("score.wav")
        score_b += 1
        pen.clear()
        pen.write("Score A: {}  score B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(340)
        play_sound("bounce.wav")
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        play_sound("bounce.wav")
        ball.dx *= -1

    # Multi-ball movement and interactions
    if (score_a == 2 or score_b == 2) and not multi_ball_active:
        activate_multi_ball()
        activate_power_up()
        
    # Multi-ball movement and interactions
    if multi_ball_active:
        extra_ball.setx(extra_ball.xcor() + extra_ball.dx)
        extra_ball.sety(extra_ball.ycor() + extra_ball.dy)

        # Border checking for extra_ball
        if extra_ball.ycor() > 290:
            extra_ball.sety(290)
            play_sound("bounce.wav")
            extra_ball.dy *= -1

        if extra_ball.ycor() < -290:
            extra_ball.sety(-290)
            play_sound("bounce.wav")
            extra_ball.dy *= -1

        if extra_ball.xcor() > 390:
            extra_ball.goto(0, 0)
            score_a += 1
            play_sound("score.wav")
            extra_ball.dx *= -1
            # Optionally, you can add scoring or other effects here

        if extra_ball.xcor() < -390:
            extra_ball.goto(0, 0)
            score_b += 1
            play_sound("score.wav")
            extra_ball.dx *= -1
            # Optionally, you can add scoring or other effects here

        # Paddle and extra_ball collisions
        if (340 < extra_ball.xcor() < 350) and (paddle_b.ycor() - 50 < extra_ball.ycor() < paddle_b.ycor() + 50):
            extra_ball.setx(340)
            play_sound("bounce.wav")
            extra_ball.dx *= -1

        if (-350 < extra_ball.xcor() < -340) and (paddle_a.ycor() - 50 < extra_ball.ycor() < paddle_a.ycor() + 50):
            extra_ball.setx(-340)
            play_sound("bounce.wav")
            extra_ball.dx *= -1

    # Check for power-up duration
    if power_up_active and time.time() - power_up_timer > 10:  # 10 seconds duration
        deactivate_power_up()

    # Randomly activate power-ups or multi-ball
    if random.randint(1, 2) == 1:  # Adjust probability as needed
        activate_power_up()  # or activate_multi_ball()

    # Game End Conditions...
    if score_a == winning_score:
        win.goto(0, 0)
        win.write("A WINS\nFinal Score\nA: {} B: {}".format(score_a, score_b), align="center", font=("Courier", 35, "normal"))
        play_sound("LevelPass.wav")
        time.sleep(3)
        Game_Run = False

    elif score_b == winning_score:
        win.goto(0, 0)
        win.write("B WINS\nFinal Score\nA: {} B: {}".format(score_a, score_b), align="center", font=("Courier", 35, "normal"))
        play_sound("LevelPass.wav")
        time.sleep(3)
        Game_Run = False
        
# Countdown timer
def countdown_timer(count):
    pen.clear()
    pen.write(f"Starting in {count}", align="center", font=("Courier", 24, "normal"))
    if count > 0:
        wn.ontimer(lambda: countdown_timer(count-1), 1000)
    else:
        pen.clear()
        pen.write("Score A: {}  score B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        main_game_loop()        
# Start the game with a countdown
countdown_timer(3)
        

turtle.done()
