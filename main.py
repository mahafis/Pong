import turtle
import winsound

wn = turtle.Screen()
wn.bgcolor("Black")
wn.title("Pong by @TheMainMufucka")
wn.setup(width=800, height=600)
wn.tracer(0)
winsound.PlaySound("powerup.wav", winsound.SND_LOOP)

# score
score_a = 0
score_b = 0

#paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.penup()
paddleA.goto(-350,0)
paddleA.shapesize(stretch_len=1, stretch_wid=5)

#paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.penup()
paddleB.goto(350,0)
paddleB.shapesize(stretch_len=1, stretch_wid=5)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1


# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {} PlayerB: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


# functions
def paddleA_up():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)
   
def paddleA_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)
   
def paddleB_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)
   
def paddleB_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)    
   
   
# keyboard binding
wn.listen()
wn.onkeypress(paddleA_up, "w")
wn.onkeypress(paddleA_down, "s")
wn.onkeypress(paddleB_up, "Up")
wn.onkeypress(paddleB_down, "Down")



#main game loop
while True:
    wn.update()
   
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
   
   
    # border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
       
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        ball.dx = 0.1
        ball.dy = 0.1
        pen.clear()
        pen.write("Player A: {} PlayerB: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
       
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        ball.dx = 0.1
        ball. dy = 0.1
        pen.clear()
        pen.write("Player A: {} PlayerB: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

       
    # paddle collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and ((ball.ycor() < paddleB.ycor() + 60) and ball.ycor() > paddleB.ycor() - 60):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.dx *= 1.1
        ball.dy *= 1.1
       
    if (ball.xcor() < -340 and  ball.xcor() > -350) and ((ball.ycor() < paddleA.ycor() + 60) and ball.ycor() > paddleA.ycor() - 60):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.dx *= 1.1
        ball.dy *= 1.1
       
       
# add music for background
# put a limit on score
# show number of round victories below
# add ai machine to challenge