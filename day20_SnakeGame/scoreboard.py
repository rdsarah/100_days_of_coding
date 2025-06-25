from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial Rounded MT Bold", 20, "bold") 
FONT_2 = ("Arial Rounded MT Bold", 26, "bold") 

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("day20_SnakeGame/data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("#ECEFF1")
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("day20_SnakeGame/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT_2)
