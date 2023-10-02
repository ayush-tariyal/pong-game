from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

my_screen = Screen()

my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("Pong game")
my_screen.tracer(0)


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkeypress(fun=l_paddle.up, key="w")
my_screen.onkeypress(fun=l_paddle.down, key="s")

my_screen.onkeypress(fun=r_paddle.up, key="i")
my_screen.onkeypress(fun=r_paddle.down, key="k")

speed = 0.1


is_game_on = True
while is_game_on:
    time.sleep(speed)
    my_screen.update()

    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # Detect collision with left and right paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (
        ball.distance(l_paddle) < 50 and ball.xcor() < -320
    ):
        ball.paddle_bounce()
        speed *= 0.9

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.ball_reset()
        scoreboard.left_scores()
        speed = 0.1

    # Detect L paddle misses
    elif ball.xcor() < -380:
        ball.ball_reset()
        scoreboard.right_score()
        speed = 0.1


my_screen.exitonclick()
