from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SCREEN_FOR_SNAKE = 252


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.lenght = len(self.snake)

    def create_snake(self):
        for i in range(3):
            new_body_part = Turtle(shape="square")
            new_body_part.color("White")
            new_body_part.penup()
            xcord = new_body_part.xcor()
            ycord = new_body_part.ycor()
            new_body_part.goto(xcord - 20 * i, ycord)
            self.snake.append(new_body_part)

    def moving(self):
        for i in range(1, len(self.snake)):
            new_coord = self.snake[-i - 1].position()
            self.snake[-i].goto(new_coord)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def snake_in_screen(self):
        head_x_position = self.head.xcor()
        head_y_position = self.head.ycor()
        if -SCREEN_FOR_SNAKE <= head_x_position <= SCREEN_FOR_SNAKE and -SCREEN_FOR_SNAKE <= head_y_position <= SCREEN_FOR_SNAKE:
            return True
        else:
            return False

    def snake_crash_herself(self):
        for body_part in self.snake[1:]:
            if self.head.distance(body_part) < 10:
                return True
        return False

    def add_body_part(self):
        new_body_part = Turtle(shape="square")
        new_body_part.color("White")
        new_body_part.penup()
        xcord = self.snake[- 1].xcor()
        ycord = self.snake[- 1].ycor()
        new_body_part.goto(xcord, ycord)
        self.snake.append(new_body_part)
