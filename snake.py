from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
shape_size = 0.8

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.body = []
        self.speed(1)
        self.penup()
        self.shapesize(shape_size)
        self.shape('square')
        self.color('white')
        self.body.append(self.create_segment())
        self.extend()


    #creates and returns new segment of body
    def create_segment(self):
        segment = Turtle(shape='square')
        segment.color('white')
        segment.shapesize(shape_size)
        segment.penup()
        return segment

    #move the snake head and body forward
    def move_forward(self):
        new_pos = self.position()
        self.forward(20)

        for segment in self.body:
            follower = segment
            prev_pos = follower.position()
            follower.setposition(new_pos)
            new_pos = prev_pos

    #add a segment to the sanke body
    def extend(self):
        pos = self.body[-1].position()
        square = self.create_segment()
        square.setposition(pos)
        self.body.append(square)

    #change snake position to
    def up(self):
        if self.heading() != DOWN:
            self.setheading(UP)

    # change snake position to
    def down(self):
        if self.heading() != UP:
            self.setheading(DOWN)

    # change snake position to
    def left(self):
        if self.heading() != RIGHT:
            self.setheading(LEFT)

    # change snake position to
    def right(self):
        if self.heading() != LEFT:
            self.setheading(RIGHT)
