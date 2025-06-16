import turtle as t
import random

screen = t.Screen()
screen.setup(height=500, width=500)
user_bet = screen.textinput("Wanna make a bet?", "Choose a color: ")
turtles_list = ["purple", "blue", "green", "yellow", "orange", "red"]
all_turtles = []
race = False

add = 0
for i in range(len(turtles_list)):
    add += 30
    tur = t.Turtle(shape="turtle")
    all_turtles.append(tur)
    tur.color(turtles_list[i])
    tur.penup()
    tur.goto(-200, -100 + add)

if user_bet:
    race = True

while race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if winner==user_bet:
                print(f"You've won! The {winner} turtle is the winner.")
            else:
                print(f"You've lost. The {winner} turtle is the winner.")
            race = False
        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)

screen.exitonclick()
