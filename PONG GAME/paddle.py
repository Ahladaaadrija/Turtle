from turtle import Turtle,Screen

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.penup()

        self.shapesize(stretch_len=5, stretch_wid=1)
        self.goto(position)
        self.left(90)

    def tup(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def tdown(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)






