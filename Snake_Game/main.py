from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍 THE SNAKE GAME 🐍")
screen.tracer(0)
snake = Snake()
food = Food()
score_board = Scoreboard()
screen.listen()

alive = True
while alive:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        alive = False
        score_board.game_over()

    for seg in snake.snake[1:]:
        if snake.head.distance(seg) < 10:
            alive = False
            score_board.game_over()

screen.exitonclick()
