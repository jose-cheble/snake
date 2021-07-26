from turtle import Screen
from snake import *
import time
from food import Food
from score import Score
from screen_art import ScreenArt

arte = ScreenArt()

screen = Screen()
screen.bgcolor("Black")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



while snake.snake_in_screen() and not snake.snake_crash_herself():
    screen.update()
    time.sleep(0.1)
    snake.moving()

#   detectar colision

    if snake.head.distance(food) < 15:
        food.refresh()
        score.sumar_punto()
        snake.add_body_part()



arte.game_over()

screen.exitonclick()
