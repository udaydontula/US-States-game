from turtle import Turtle, Screen
import pandas
import turtle

screen = Screen()

image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(height=491, width=725)
turtle.shape(image)
screen.title("US States Game")
guessed_state = []
missed_list = []

while len(guessed_state) < 50:
    answer = screen.textinput(title=f"{len(guessed_state)}/50", prompt="Enter the state name:").title()
    data = pandas.read_csv("50_states.csv")
    state_list = data["state"].tolist()

    if answer == "Exit":
        missed_list = [state for state in state_list if state not in guessed_state]
        new_file = pandas.DataFrame(missed_list)
        new_file.to_csv("State_to_learn.csv")
        break

    if answer in state_list:
        state_data = data[data.state == answer]
        guessed_state.append(answer)
        t = Turtle()
        t.penup()
        t.hideturtle()
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(answer)



