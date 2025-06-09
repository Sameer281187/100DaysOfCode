import random
from turtle import Turtle, Screen

screen = Screen()
screen.screensize(canvwidth=600, canvheight=400)
is_race_on = False
user_bet = screen.textinput("Make a bet!", "Select a turtle who would win this race? Enter color name: ")

turtle_colors = ["indigo", "blue", "green", "yellow", "orange", "red"]
turtle_pos = [-220, -130, -40, 50, 140, 230]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(turtle_colors[turtle_index])
    new_turtle.goto(-300, turtle_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for t in all_turtles:
        if t.xcor() > 350:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print(f"You win! {winning_color} turtle won the race.")
            else:
                print(f"You lose! {winning_color} turtle won the race.")
        turtle_step = random.randint(0,11)
        t.forward(turtle_step)


screen.exitonclick()