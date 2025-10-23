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

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").lower()



def check_state():
    for state in states:
        if answer_state == state.lower():
            state_data_x = data[data["state"] == state].x.item()
            stata_data_y = data[data["state"] == state].y.item()
            return state_data_x, stata_data_y
    return False




def draw_state(coords):
    x, y = coords
    city.goto(x, y)
    city.write(f"{answer_state}", font=style)






game_on = True
while game_on:
    check_state()
    found_state = check_state()
    if found_state:
        draw_state(found_state)
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").lower()

turtle.mainloop()



