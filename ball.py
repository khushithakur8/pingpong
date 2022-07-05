from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("deep pink")
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.xmove = 10
        self.ymove = 10

    def move(self):
        new_x = self.xcor()+self.xmove
        new_y = self.ycor()+self.ymove
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.ymove = self.ymove * -1

    def x_bounce(self):
        self.xmove = self.xmove * -1

    def reset_position(self):
        self.goto(0, 0)
        self.x_bounce()
