from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.refresh()

    def refresh(self):
        shape = random.choice(["square", "circle", "triangle"])
        color = random.choice(["red", "yellow", "orange"])
        self.hideturtle()
        self.shape(shape)
        self.color(color)
        self.goto(random.randint(-350, 350), random.randint(-250,250))
        self.showturtle()