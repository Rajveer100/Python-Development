from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(False)

screen.title("My Snake Game")

snake = Snake()
food = Food()
score = Score()

game_is_running = True

screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

while game_is_running:

    screen.update()
    time.sleep(0.135)

    snake.move()

    if snake.head.distance(food) < 15:

        food.new_location()

        score.update_score()
        snake.grow()

    if snake.did_hit_wall() or snake.did_collide_itself():

        game_is_running = False
        score.game_over()

screen.exitonclick()
