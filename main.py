import turtle
from turtle import Turtle, Screen
import random

is_race_on=False
screen = Screen()
screen.setup(500,400)
user_bet=screen.textinput("Make Your Bet", "Which turtle will win the race? Enter a colour: ").lower()
colors=["red","orange","yellow","green","blue","indigo","violet"]
y_positions=[-160,-110,-60,-10,40,90,130]
all_turtles=[]

for create_turtle in range(0,6):
    new_turtle=Turtle("turtle")
    new_turtle.color(colors[create_turtle])
    new_turtle.penup()
    new_turtle.goto(-230, y=y_positions[create_turtle])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtles in all_turtles:
        if turtles.xcor() > 220:
            is_race_on=False
            winning_color = turtles.pencolor()
            if winning_color==user_bet:
                print(f"You won! The {winning_color} is the winner")
            else:
                print(f"You lost! The {winning_color} is the winner")

        rand_distance=random.randint(0,10)
        turtles.forward(rand_distance)
screen.exitonclick()