from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import ScoreBoard

import time
screen=Screen()
screen.bgcolor('black')
screen.setup(width=600,height=600)
screen.title('Snake Game')
screen.tracer(0)
snake=Snake()
food=Food()
score=ScoreBoard()
screen.listen()
screen.onkey(fun=snake.up,key='Up')
screen.onkey(fun=snake.down,key='Down')
screen.onkey(fun=snake.left,key='Left')
screen.onkey(fun=snake.right,key='Right')
    
is_game_on=True


while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food)<15:
        score.increas_score()
        food.refresh()
        snake.extend()
    if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-280 or snake.segments[0].ycor()>280 or snake.segments[0].ycor()<-280:
        score.reset_scoreboard()
        snake.reset_snake()
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment)<10:
            score.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()