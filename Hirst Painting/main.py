import turtle

import colorgram
from turtle import Turtle, Screen
import random

# rgb_colors = []
# colors = colorgram.extract("Hirst_Image.png", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)
#
# print(rgb_colors)

subish = Turtle()
turtle.colormode(255)
screen = Screen()
subish.hideturtle()
subish.speed("fastest")

color_list = [(234, 233, 231), (233, 222, 228), (190, 172, 0), (208, 0, 103), (0, 148, 60), (253, 69, 0),
              (217, 229, 234), (167, 0, 0), (0, 128, 205), (89, 0, 95), (254, 223, 0), (232, 234, 232), (42, 192, 234),
              (0, 0, 0), (248, 19, 152), (253, 7, 4), (235, 11, 143), (253, 4, 6), (15, 190, 234), (236, 153, 69),
              (250, 51, 17), (238, 215, 82), (16, 167, 127), (224, 126, 168), (234, 163, 190), (114, 193, 156),
              (160, 210, 177), (142, 209, 228), (239, 170, 157), (106, 120, 184)]


def set_position():
    subish.setheading(225)
    subish.penup()
    subish.forward(400)
    subish.setheading(0)


def background():
    subish.color("white smoke")
    subish.begin_fill()
    for i in range(4):
        subish.forward(660)
        subish.left(90)
    subish.end_fill()


def print_dot():
    subish.setposition(subish.xcor() + 60, subish.ycor() + 60)
    for row in range(10):
        for column in range(10):
            subish.dot(18, random.choice(color_list))
            subish.penup()
            subish.forward(60)
            subish.pendown()

        subish.penup()
        subish.setposition(subish.xcor()-600, subish.ycor()+60)


set_position()
background()
print_dot()


screen.exitonclick()
