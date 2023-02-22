from turtle import Screen
from food import Food
from snake import Snake
from score import ScoreBoard
import time


screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Blue Snake")
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
score = ScoreBoard()

screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        score.clear()
        score.print_score()
        snake.extend_tail()

    # Detect wall collision
    if snake.hit_wall():
        game_on = False
        score.game_over()

    # Detect tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()


screen.exitonclick()
