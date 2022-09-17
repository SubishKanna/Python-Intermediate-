import turtle
from turtle import Turtle, Screen
import random

subish = Turtle()
screen = Screen()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    ra_color = (r, g, b)
    return ra_color


def square():
    subish.begin_fill()
    for _ in range(4):
        subish.fd(150)
        subish.left(90)

    subish.end_fill()
    subish.color("black", "yellow")


def dashed_line():
    for _ in range(10):
        subish.pendown()
        subish.forward(10)
        subish.penup()
        subish.forward(10)


def different_shapes():
    for i in range(3, 11, 1):
        degree = 360
        degree /= i
        subish.color(random.choice(r, g, b))
        subish.pensize(i)
        for j in range(i):
            subish.forward(100)
            subish.right(degree)


def random_walk():
    angles = [0, 90, 180, 270]

    for _ in range(300):
        subish.width(10)
        subish.color(random_color())
        subish.speed(0)
        subish.forward(40)
        subish.setheading(random.choice(angles))


def spirograph(size):
    subish.speed(0)
    for i in range(int(360 / size)):
        subish.color(random_color())
        subish.circle(100)
        subish.setheading(subish.heading() + size)


#spirograph(6)

screen.exitonclick()
