from turtle import Turtle
ALIGNAMENT = "center"
FONT = ("Arial", 15, "normal")
TEXT_SIZE = 15


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.actualizar_score()

    def actualizar_score(self):
        self.write(f"Score: {self.score}", align=ALIGNAMENT, font=FONT)

    def sumar_punto(self):
        self.score += 1
        self.clear()
        self.actualizar_score()
