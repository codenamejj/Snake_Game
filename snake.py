from turtle import Turtle, Screen

screen = Screen()

ELEMENT_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in ELEMENT_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_block = Turtle(shape="square")
        new_block.color("white")
        new_block.penup()
        new_block.goto(position)
        self.segments.append(new_block)

    def extend_tail(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_index in range(len(self.segments) - 1, 0, -1):
            x_position = self.segments[seg_index - 1].xcor()
            y_position = self.segments[seg_index - 1].ycor()
            self.segments[seg_index].goto(x_position, y_position)

        self.head.forward(MOVE_DISTANCE)

    def hit_wall(self):
        """returns True if the snake head hits the wall, otherwise, returns False"""
        if self.head.xcor() > 299 or self.head.xcor() < - 299 or self.head.ycor() > 299 or self.head.ycor() < - 299:
            return True

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
