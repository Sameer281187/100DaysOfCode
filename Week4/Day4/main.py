import turtle
from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
states_data = pandas.read_csv("50_states.csv")
score = 0
guessed_states = []
missed_states = []

while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"{score}/50 states correct", prompt="What's another state's name ?").title()
    if user_answer == "Exit":
        for st in states_data.state:
            if not guessed_states.__contains__(st):
                missed_states.append(st)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break

    for st in states_data.state:
        if st == user_answer:
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.hideturtle()
            entered_state_data = states_data[states_data["state"] == st]
            xcor = entered_state_data.x.item()
            ycor = entered_state_data.y.item()
            new_turtle.goto(xcor, ycor)
            new_turtle.write(st, align= "center", font= ("Ariel", 8, "normal"))
            score += 1
            guessed_states.append(user_answer)
            break


