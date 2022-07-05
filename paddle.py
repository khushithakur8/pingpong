from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("turquoise")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def go_up(self):
        y = self.ycor()
        new_y = y+20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        y = self.ycor()
        new_y = y-20
        self.goto(self.xcor(), new_y)


