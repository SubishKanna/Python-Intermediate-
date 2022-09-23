import turtle
from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
y_pos = [-70, -40, -10, 20, 50, 80]
user_input = screen.textinput(title="What's your bet", prompt="Which turtle will win the race? Enter a color: ")
colour = ["red", "green", "yellow", "purple", "blue", "black"]
all_turtle = []

for turtle_index in range(len(colour)):
    new_turtle = Turtle("turtle")
    new_turtle.color(colour[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtle.append(new_turtle)

is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
