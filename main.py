import turtle
import time
import pandas
from map_turtle import MapTurtle


#Panda stuff
state_data = pandas.read_csv("50_states.csv")
state = state_data["state"]
state_to_list = state.to_list()
location_x_list = state_data["x"].to_list()
location_y_list = state_data["y"].to_list()

#setting screen name
screen = turtle.Screen()
screen.title = ("U.S. States Game")

#setting screen_size
screen.setup(width=725, height=491)

#Turtle

jeff = MapTurtle()



#Setting the turtle background Image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# answer_state_title = answer_state.title()

guessed_states = []
score = len(guessed_states)
amount_of_states = len(state_to_list)

while score < amount_of_states:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(state_to_list)} Correct states!", prompt="What's another state's name?").title()
    screen.update()
    time.sleep(0.1)

    #Other way i did using the index (but ended up finding easier way through panda)
    # state_index = state_to_list.index(answer_state)
    # new_x_value = location_x_list[state_index]
    # new_y_value = location_y_list[state_index]

    #Setting user_state = the data that the answer would be at calling it
    user_state = state_data[state == answer_state]
    if answer_state in state_to_list:
        guessed_states.append(answer_state)
        # x and y being the value in the same row but different columns
        jeff.right_answer(answer_state, user_state.x, user_state.y)
        #Test for the answer using INDEX
        # print(state_index)
        # print(new_x_value)
        # print(new_y_value)
        print("Oh wow that exists?!")

    elif answer_state == "Exit":
        missing_state = []
        for state in state_to_list:
            if state not in guessed_states:
                missing_state.append(state)

        forgotten_states = {
            "missing states": missing_state}
        forgotten_states_data = pandas.DataFrame(forgotten_states)
        forgotten_states_data.to_csv("forgotten_states.csv")
        break

    else:
        print("nuh uh this doesnt exist")





##Get click cordinates
# def get_mouse_click_cor(x, y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)




turtle.mainloop()