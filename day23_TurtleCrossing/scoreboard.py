from turtle import Turtle

FONT = ("Courier", 24, "normal")
GAMEOVER_FONT = ("Courier", 30, "bold")
POSITION = (-200, 240)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(POSITION)
        self.write(f"Level:{self.score}", align="center", font=FONT)

    def points(self):
        self.score += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=GAMEOVER_FONT)
        self.goto(0, -50)
        self.write(f"Final score: {self.score}", align="center", font=FONT)
