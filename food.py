from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed('fastest')
        self.color('cyan')
        self.goto(x=randint(-220, 220), y=randint(-220, 220))

    # change position of food
    def refresh(self):
        self.goto(x=randint(-220, 220), y=randint(-220, 220))
