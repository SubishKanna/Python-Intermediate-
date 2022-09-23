import turtle
from turtle import Turtle, Screen

subish = Turtle()
screen = Screen()
screen.listen()


def move_forward():
    turtle.forward(15)


def backwards():
    turtle.backward(15)


def counter_clockwise():
    turtle.left(30)


def clockwise():
    turtle.right(30)


def clear_drawing():
    turtle.reset()


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s",  fun=backwards)
screen.onkey(key="a",  fun=counter_clockwise)
screen.onkey(key="d",  fun=clockwise)
screen.onkey(key="c",  fun=clear_drawing)

screen.exitonclick()
