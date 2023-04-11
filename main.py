from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreborad

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


segments = []

snake = Snake()
food = Food()
score_board = Scoreborad()

screen.listen()
screen.onkey(snake.up_key, "Up")
screen.onkey(snake.down_key, "Down")
screen.onkey(snake.left_key, "Left")
screen.onkey(snake.right_key, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    

    # detect colision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
    
    # detect colison with wall
    if snake.head.xcor() > 280:
        snake.right_wall_colision()

    if snake.head.xcor() < -280:
        snake.left_wall_colision()

    if snake.head.ycor() > 280:
        snake.up_wall_colision()

    if snake.head.ycor() < -280:
        snake.down_wall_colision()


     
        


screen.exitonclick()