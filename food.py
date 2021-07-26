from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.color("Blue")

    def refresh(self):
        random_x = randint(-240, 240)
        random_y = randint(-240, 240)
        self.goto(random_x, random_y)
