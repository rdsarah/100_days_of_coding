from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
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
            self.add_segment(position)
            
    def add_segment(self, position):
        sn_segment = Turtle("square")
        sn_segment.color("#90CAF9")
        sn_segment.penup()
        sn_segment.goto(position)
        self.segments.append(sn_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.seth(UP)
    
    def down(self):
        if self.head.heading()!=UP:
            self.head.seth(DOWN)
    
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.seth(RIGHT)

    def reset_snake(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
