from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400) #Setting window with fixed width and height
screen.bgpic("sand.gif")
user_input = screen.textinput(title="Tortoise Race",
                              prompt="Choose a Tortoise:\n"
                                     "red, blue, green, yellow, orange, purple")
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
x_axis =-230.00
y_axis =-90.00
all_turtles = []

for i in range(6):
    turtle = Turtle(shape="turtle")  # Defaulting class with marker shape like turtle
    turtle.penup()
    turtle.speed(10)
    turtle.color("SaddleBrown", colors[i])
    turtle.goto(x_axis, y_axis)
    y_axis += 35
    all_turtles.append(turtle)

game_on = False

if user_input:
    game_on = True

while game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            game_on = False
            winner_color = turtle.fillcolor()
            if winner_color == user_input:
                print(f"You Win 👍 !!! The {winner_color} Turtle is the Winner 🐢.")
            else:
                print(f"You've Lost 👎 !!! The {winner_color} Turtle is the Winner 🐢.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()



