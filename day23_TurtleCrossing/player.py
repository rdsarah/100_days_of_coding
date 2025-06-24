from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
DIRECTION = 90


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.seth(DIRECTION)
        self.penup()
        self.restart_player()
    
    def move_player(self):
        self.forward(MOVE_DISTANCE)
    
    def goal(self):
        return self.ycor() > FINISH_LINE_Y

    def restart_player(self):
        self.goto(STARTING_POSITION)
