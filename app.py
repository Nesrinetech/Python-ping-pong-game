#imported turtle module
import turtle 

wind = turtle.Screen() #intialize screen
wind.title("Ping Pong By Nesrine") #set the title of the window
wind.bgcolor("black") #set the backgroun color of the window
wind.setup(width=800, height=600) #set the width and height of the window
wind.tracer(0) #stops the window from updating automatically

#madrab1
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("blue")
madrab1.shapesize(stretch_wid=5, stretch_len=1)
madrab1.penup()
madrab1.goto(-350,0)

#madrab2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.penup()
madrab2.goto(350,0)

#ball    
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0 Player 2: 0", align="center", font=("Courier",24,"normal"))

#functions
def madrab1_up():
    y = madrab1.ycor() 
    y += 20
    madrab1.sety(y)
    
def madrab1_down():
    y = madrab1.ycor()
    y -= 20
    madrab1.sety(y)
    
def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)
    
def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)
    
#keyboard bindings
wind.listen() #tell the window to expect keyboard input
wind.onkeypress(madrab1_up, "w") #when pressing w the function madrab1_up is invoked
wind.onkeypress(madrab1_down, "s")
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")
#main game loop
while True:
    wind.update() #updates the screen everytime the loop run
    
    #move the ball
    ball.setx(ball.xcor() + ball.dx) #ball starts at 0 and everytime loops run--->+0.5 xaxis
    ball.sety(ball.ycor() + ball.dy) #ball starts at 0 and everytime loops run--->+0.5 yaxis
    
    #border check , top border +300px, bottom border -300px, ball is 20px
    if ball.ycor() >290: #if ball is at top border
        ball.sety(290) #set y coordinate +290
        ball.dy *= -1 #reverse direction, making +0.5--->-0.5
        
    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor() >390: # if ball is at right border
        ball.goto(0, 0)  #return ball to center 
        ball.dx *= -1    #reverse the x direction 
        score1 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier",24,"normal"))
        
    if ball.xcor() <-390: # if ball is at left border
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier",24,"normal"))
    #tasadom madrab and ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1 