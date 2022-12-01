from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")


game_on = True

while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect paddle1 missing
    if ball.xcor() > 400:
        scoreboard.points1()
        ball.reset_pos()

    # detect paddle2 missing
    if ball.xcor() < -400:
        scoreboard.points2()
        ball.reset_pos()


screen.exitonclick()
