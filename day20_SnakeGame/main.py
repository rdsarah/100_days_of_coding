from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
    
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("#263238")
screen.title("Snakies")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    #Detect collision with the wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        scoreboard.reset()
        snake.reset_snake()
        
    #Detect collision with tail
    for segment in snake.segments[1:]:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset_snake()

screen.exitonclick()
