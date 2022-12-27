from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.title("PONG GAME")
screen.bgcolor("black")
screen.tracer(0)
ball = Ball()
score = Score()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

# paddle = Turtle("square")
# paddle.color("white")
# paddle.shapesize(stretch_len=1, stretch_wid=5)
# paddle.penup()
# paddle.goto(350, 0)
#
# def go_up():
#
#      new_y = paddle.ycor() + 20
#      paddle.goto(paddle.xcor(), new_y)
#
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)
#

r_paddle.go_up()
r_paddle.go_down()
l_paddle.go_up()
l_paddle.go_down()
r_paddle.speed('fastest')
l_paddle.speed('fastest')


screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")




game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() >320 and  ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() >380:
        ball.center()
        score.l_point()

    if ball.xcor() <-380:
        ball.center()
        score.r_point()



screen.exitonclick()
