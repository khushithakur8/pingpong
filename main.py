from turtle import Screen, Turtle
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard
from net import Net

start = Turtle()
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Ping Pong")

screen.tracer(0)

r_paddle = Paddle(375, 0)
l_paddle = Paddle(-375, 0)
ball = Ball()


screen.listen()

screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)


net = Net()

start.color("magenta")
start.write("Welcome to Khushi's Ping Pong Game! Press space to start", align="center", font=("Courier", 18, "italic"))
start.hideturtle()


def game():
    game_is_on = True
    start.clear()
    score = Scoreboard()
    score.update()
    pace = 0.1
    net.net_make()
    while game_is_on:

        time.sleep(pace)
        screen.update()
        ball.move()

        if ball.ycor() > 270 or ball.ycor() < -270:
            ball.y_bounce()
            pace = pace-0.0025

        if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
            ball.x_bounce()
            pace = pace-0.005

        # right player misses
        if ball.xcor() > 390:
            ball.reset_position()
            score.r_miss()
            pace = 0.1

        if ball.xcor() < -390:
            ball.reset_position()
            score.l_miss()
            pace = 0.1

        if score.rscore == 10 or score.lscore == 10:
            score.game_over()
            game_is_on = False


screen.onkey(key="space", fun=game)


screen.exitonclick()