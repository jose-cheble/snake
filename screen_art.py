from turtle import Turtle
SCREEN_LIMIT = 250

class ScreenArt(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color("White")
        self.crear_limites()

    def crear_limites(self):
        self.goto(-SCREEN_LIMIT, -SCREEN_LIMIT)
        self.pendown()
        self.goto(SCREEN_LIMIT, -SCREEN_LIMIT)
        self.goto(SCREEN_LIMIT, SCREEN_LIMIT)
        self.goto(-SCREEN_LIMIT, SCREEN_LIMIT)
        self.goto(-SCREEN_LIMIT, -SCREEN_LIMIT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 15))