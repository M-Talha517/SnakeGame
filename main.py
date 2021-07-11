from turtle import Screen, Turtle
import snake
import time
import food
from scoreboard import Scoreboard

screenwidth = 500
screenheight = 500
screen = Screen()
screen.setup(width=screenwidth, height=screenheight)
screen.bgcolor('black')
screen.title('SNAKE MANIA')
screen.tracer(0)

sanp = snake.Snake()
khana = food.Food()
scoreboard = Scoreboard(screenheight / 2)
game_speed = 0.1

screen.listen()
screen.onkey(sanp.up, "Up")
screen.onkey(sanp.down, "Down")
screen.onkey(sanp.left, "Left")
screen.onkey(sanp.right, "Right")


def boundary_maker(turtle):
    turtle.penup()
    turtle.pencolor('white')
    turtle.goto(screenwidth // 2, screenheight // 2)
    turtle.pendown()
    turtle.pensize(4)
    turtle.hideturtle()
    for i in range(4):
        turtle.right(90)
        turtle.forward(screenheight) if i % 2 == 0 else turtle.forward(screenwidth)


def main():
    boundary_maker(Turtle())
    game_over = False
    screen.update()
    while not game_over:
        time.sleep(game_speed)
        sanp.move_forward()

        # check snake collision with food
        if sanp.distance(khana) < 15:
            khana.refresh()
            scoreboard.add_score()
            sanp.extend()

        # check snake collision with wall
        if sanp.xcor() <= -(screenwidth // 2 - 20) or sanp.xcor() >= (screenwidth // 2 - 20) or \
                sanp.ycor() <= -(screenheight // 2 - 20) or sanp.ycor() >= (screenheight // 2 - 20):
            game_over = True

        # check snake collision with body
        for segment in sanp.body:
            if sanp.position() == segment.position():
                game_over = True

        screen.update()
    khana.hideturtle()
    screen.update()
    scoreboard.game_over()


main()
screen.exitonclick()
