
from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
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
        for position in STARTING_POSITIONS:
            new_segemnt = Turtle("square")
            new_segemnt.color("white")
            new_segemnt.penup()
            new_segemnt.goto(position)
            self.segments.append(new_segemnt)
    
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up_key(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    
    def down_key(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    

    def left_key(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    

    def right_key(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    


    def up_wall_colision(self):
        if self.head.heading() == UP:
            self.head.setheading(DOWN)

    
    def down_wall_colision(self):
        if self.head.heading() == DOWN:
            self.head.setheading(UP)
    

    def right_wall_colision(self):
        if self.head.heading() == RIGHT:
            self.head.setheading(LEFT)
    

    def left_wall_colision(self):
        if self.head.heading() == LEFT:
            self.head.setheading(RIGHT)