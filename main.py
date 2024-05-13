import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

dataset = pd.read_csv("50_states.csv")
states = list(dataset["state"])

game_is_on = True

count = 0
correct_states = []


def state_finish(us_state):
    state_series = dataset[dataset["state"] == us_state]
    x = int(state_series["x"])
    y = int(state_series["y"])
    writer = turtle.Turtle()
    writer.penup()
    writer.hideturtle()
    writer.goto(x, y)
    writer.write(us_state, align="center", font=("SF Pro Display", 10, "bold"))


def generate_csv():
    final_list = [s for s in states if s not in correct_states]
    remnant_states = pd.DataFrame(final_list)
    remnant_states.to_csv("remnant_states.csv")


answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()

while game_is_on:
    if count == 0:
        pass
    else:
        answer_state = screen.textinput(title=f"{count}/50 correct", prompt="What's another state's name?").title()
        if answer_state.lower() == "exit":
            if not (len(correct_states)) == 0:
                generate_csv()
                game_is_on = False
    for state in states:
        if answer_state == state:
            state_finish(us_state=answer_state)
            count += 1
            correct_states.append(answer_state)
            if count == 50:
                game_is_on = False
    if answer_state not in states:
        print("it is not a USA State.")
