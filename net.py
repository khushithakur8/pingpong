from turtle import Turtle


class Net(Turtle):

    def __init__(self):
        super().__init__()

    def net_make(self):
        self.color("white")
        self.hideturtle()
        self.pensize(3)
        self.making()

    def making(self):
        self.goto(0, 0)
        self.setheading(90)
        while self.ycor()<300:
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
        self.penup()
        self.goto(0, 0)
        self.setheading(-90)
        while self.ycor()>-300:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)






