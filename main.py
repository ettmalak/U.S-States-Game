import turtle, pandas
from errno import ELOOP
from turtle import Turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
style = ('Courier', 10, 'normal')
city = Turtle()
city.hideturtle()
city.penup()

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
coordinates = []
guessed_states = []



answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state's name?").title()



def check_state():
    for state in states:
        if answer_state == state:
            state_data_x = data[data["state"] == state].x.item()
            stata_data_y = data[data["state"] == state].y.item()
            guessed_states.append(answer_state)
            return state_data_x, stata_data_y
    return False




def draw_state(coords):
    x, y = coords
    city.goto(x, y)
    city.write(f"{answer_state}", font=style)



while len(guessed_states) < 50:
    found_state = check_state()
    if found_state:
        draw_state(found_state)
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
            df = pandas.DataFrame(missing_states)
            df.to_csv("states_to_learn.csv", index = False)

        break



#states_to_learn.csv

