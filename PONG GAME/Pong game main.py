from turtle import Turtle,Screen
import random
from paddle import Paddle
from ball import Ball
import time
from score import Score

game_start = True
ball = Ball()
s = Screen()
t = Turtle()
s.bgcolor("Black")
s.setup(800, 600)
s.title("Pong")
s.tracer()


right = Paddle((350,0))
left = Paddle((-350,0))


s.listen()
s.onkey(right.tup, "Up")
s.onkey(right.tdown, "Down")
s.onkey(left.tup, "w")
s.onkey(left.tdown, "s")

score = Score()

while game_start:
    time.sleep(.1)
    s.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right) < 50 and ball.xcor() > 320:

        ball.bounce_x()

    if ball.distance(left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor()>390:
        score.increase_left()
        ball.reset()
    if ball.xcor()<-390:
        score.increase_right()
        ball.reset()








s.exitonclick()
s.mainloop()
