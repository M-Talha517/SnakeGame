from turtle import Turtle, Screen

t = Turtle()

screen = Screen()
screen.listen()


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def turn_clockwise():
    t.right(5)


def turn_anticlockwise():
    t.left(5)


def reset():
    t.penup()
    t.clear()
    t.home()
    t.pendown()


screen.exitonclick()