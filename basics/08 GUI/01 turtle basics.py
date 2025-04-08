import turtle
import random

t = turtle.Turtle()

t.forward(100)
t.right(45)
t.forward(50)
t.left(90)
t.backward(50)
t.penup()

t.goto(0, 0)
t.pendown()

for i in range(20):
    t.color(random.choice(["red", "green", "blue", "yellow"]))
    t.width(i + 1)
    t.forward(70 + 20*i)
    t.right(90)

turtle.mainloop()
