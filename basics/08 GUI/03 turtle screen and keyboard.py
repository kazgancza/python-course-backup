import turtle
import time

t = turtle.Turtle()
win = turtle.Screen()

win.title(__name__)
win.bgcolor("black")
win.setup(width=800, height=600)

t.color("white")
t.forward(100)
print("x: ", t.xcor())
print("y: ", t.ycor())

def key_pressed_w():
    print("w clicked")
    t.fd(20)

def key_pressed_s():
    print("s clicked")
    t.bk(20)

win.listen()
win.onkey(key_pressed_w, "w")
win.onkey(key_pressed_s, "s")

win.tracer(0)

while True:
    win.update()
    time.sleep(0.01)

win.mainloop()