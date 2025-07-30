from turtle import Turtle
import random
pos = ["x","y"]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.x=10
        self.y=10
        self.move_speed = 3
        self.penup()

        self.goto(random.randint(-280, 280), random.randint(-280, 280))

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x,new_y)

    def bounce_x(self):
        self.x *= -1
        self.move_speed *= 0.9

    def bounce_y(self):
        self.y *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0,0)
        self.move_speed *= 0.9
        self.h = random.choice(pos)
        self.h *= -1
        self.move()







    


