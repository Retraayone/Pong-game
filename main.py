import turtle 

win = turtle.Screen()
win.title("Pong By @retraayone")
win.bgcolor("black")
win.setup(width = 1280, height = 720)
win.tracer(0) #stops the window from updating


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-450,0)


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(450,0)

# ball
ball = turtle.Turtle()  
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = -2


#Function
def paddle_a_up():
    y = paddle_a.ycor()
    y+= 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y+= 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


win.listen()
win.onkeypress(paddle_a_up,"w")
win.onkeypress(paddle_a_down,"s")
win.onkeypress(paddle_b_up,"Up")
win.onkeypress(paddle_b_down,"Down")

ball_radius = 10  # Assuming the ball's radius is 10 pixels
effective_y_range = (720 / 2) - ball_radius
effective_x_range = (1280 / 2) - ball_radius


# main game loop
while True:
    win.update()

    # move the ball
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
        ball.setx(effective_x_range)
        ball.dx *= -1

    if ball.xcor() < -effective_x_range:
        ball.setx(-effective_x_range)
        ball.dx *= -1
