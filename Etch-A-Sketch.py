# Event Listener are so important to experience the program
# We can say it as Function as Inputs
# A screen waiting for an Input to execute a function
# e.g., executing a function while pressing a key

# Etch-A-Sketch Project:

# We can create many objects from same class
# Which means these objects (Instances) are independent
# and have its own attributes (state)
# e.g., turtle01 in green color, turtle02 in red color
# e.g., turtle01 in large size, turtle02 small size etc...

from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

turtle.shape("arrow")
turtle.shapesize(1.0, 1.0, 0.5)
screen.bgpic("board.gif")
turtle.color("gold", "black")

def move_forward():
    turtle.forward(10)

def turn_backward():
    turtle.right(180)

def turn_left():
    turtle.left(10)

def turn_right():
    turtle.right(10)

def clear():
    turtle.clear()
    pen_up()
    turtle.home()
    pen_down()

def pen_up():
    turtle.penup()

def pen_down():
    turtle.pendown()

screen.listen() #This will make the screen to looking for an Input
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=turn_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.onkey(key="x", fun=pen_up)
screen.onkey(key="v", fun=pen_down)
# Note: The above is called Higher Order Function
# i.e., A function works within another function
# the function within function dont needs to be given ()

screen.exitonclick()
