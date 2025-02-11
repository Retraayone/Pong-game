import turtle

win = turtle.Screen()
win.title("Pong By @retraayone")
win.bgcolor("black")
win.setup(width=1280, height=720)
win.tracer(0)  # stops the window from updating

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-450, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(450, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# Score variables
score_a = 0
score_b = 0

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function to update the score display
def update_score():
    score_display.clear()
    score_display.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

# Function to check for a winner
def check_winner():
    if score_a >= 5:
        score_display.goto(0, 0)
        score_display.write("Player A Wins!", align="center", font=("Courier", 36, "normal"))
        return True
    elif score_b >= 5:
        score_display.goto(0, 0)
        score_display.write("Player B Wins!", align="center", font=("Courier", 36, "normal"))
        return True
    return False

# Paddle movement variables
paddle_a_speed = 20
paddle_b_speed = 20
paddle_a_direction = 0
paddle_b_direction = 0

# Function to move paddle A
def move_paddle_a():
    y = paddle_a.ycor() + paddle_a_direction
    if y > 310:
        y = 310
    if y < -310:
        y = -310
    paddle_a.sety(y)
    win.ontimer(move_paddle_a, 20)

# Function to move paddle B
def move_paddle_b():
    y = paddle_b.ycor() + paddle_b_direction
    if y > 310:
        y = 310
    if y < -310:
        y = -310
    paddle_b.sety(y)
    win.ontimer(move_paddle_b, 20)

# Functions to change paddle direction
def paddle_a_up():
    global paddle_a_direction
    paddle_a_direction = paddle_a_speed

def paddle_a_down():
    global paddle_a_direction
    paddle_a_direction = -paddle_a_speed

def paddle_a_stop():
    global paddle_a_direction
    paddle_a_direction = 0

def paddle_b_up():
    global paddle_b_direction
    paddle_b_direction = paddle_b_speed

def paddle_b_down():
    global paddle_b_direction
    paddle_b_direction = -paddle_b_speed

def paddle_b_stop():
    global paddle_b_direction
    paddle_b_direction = 0

# Keyboard bindings
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeyrelease(paddle_a_stop, "w")
win.onkeyrelease(paddle_a_stop, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")
win.onkeyrelease(paddle_b_stop, "Up")
win.onkeyrelease(paddle_b_stop, "Down")

# Start moving paddles
move_paddle_a()
move_paddle_b()

ball_radius = 10  # Assuming the ball's radius is 10 pixels
effective_y_range = (720 / 2) - ball_radius
effective_x_range = (1280 / 2) - ball_radius

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > effective_y_range:
        ball.sety(effective_y_range)
        ball.dy *= -1

    if ball.ycor() < -effective_y_range:
        ball.sety(-effective_y_range)
        ball.dy *= -1

    if ball.xcor() > effective_x_range:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        update_score()
        if check_winner():
            break

    if ball.xcor() < -effective_x_range:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        update_score()
        if check_winner():
            break

    # Paddle and ball collision
    if (ball.xcor() > 440 and ball.xcor() < 450) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(440)
        ball.dx *= -1

    if (ball.xcor() < -440 and ball.xcor() > -450) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-440)
        ball.dx *= -1