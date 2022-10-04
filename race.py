import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
color = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
a = 0
c = random.sample(color, k=6)
all_turtles = []
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(c[i])
    new_turtle.goto(-230, -100 + a)
    all_turtles.append(new_turtle)
    a += 50
if bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            a = turtle.color()
            if bet == a[0]:
                print(f"Correct guess, {a[0]} is winner")
            else:
                print(f"Wrong guess, {a[1]} is not the winner")
            is_race_on = False
            break
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
