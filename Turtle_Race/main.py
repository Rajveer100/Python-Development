import random
from turtle import Turtle, Screen

cur_screen = Screen()
cur_screen.setup(width=500, height=500)

bet_colour = cur_screen.textinput(title="Which turtle would win ?", prompt="Enter a colour: ")

turtle_colours = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
turtles = [Turtle(shape="turtle") for _ in range(7)]

for i in range(7):

    turtles[i].color(turtle_colours[i])
    turtles[i].penup()

    if i == 0:

        turtles[i].goto(-220, 0)
    elif i <= 3:

        turtles[i].goto(-220, 0 + 60 * i)
    else:

        turtles[i].goto(-220, 0 + -60 * (i - 3))

win_colour = "?"
race_ended = False

while not race_ended:

    for i in range(7):

        rnd_dist = random.randint(1, 10)
        turtles[i].forward(rnd_dist)

        if turtles[i].xcor() >= 250:

            win_colour = turtles[i].color()

            race_ended = True
            break

if win_colour == bet_colour:

    cur_screen.title("You Win!")
else:

    cur_screen.title("You Lose!")

cur_screen.exitonclick()

