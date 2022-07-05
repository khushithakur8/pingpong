from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.rscore = 0
        self.lscore = 0
        self.hideturtle()
        self.penup()
        self.update()

    def update(self):
        self.clear()
        self.color("white")
        self.goto(-100, 200)
        self.write(self.lscore, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("Courier", 80, "normal"))

    def r_miss(self):
        self.lscore+=1
        self.update()

    def l_miss(self):
        self.rscore+=1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.color("spring green")
        if self.rscore == 10:
            self.write("Right player Won! Game over", align="center", font=("Courier", 18, "normal"))
        if self.lscore == 10:
            self.write("Left player Won! Game over", align="center", font=("Courier", 18, "normal"))




