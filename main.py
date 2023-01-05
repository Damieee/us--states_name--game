import turtle
import pandas
from game_brain import GameBrain

game_brain=GameBrain()
screen=turtle.Screen()
screen.setup(height=491, width=725)
screen.title("U.S. STATES GAME")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states=[]
empty_states=[]

data=pandas.read_csv("50_states.csv")
states_list=data.state.to_list()

while len(states)<50:
    answer_state=screen.textinput(title=f"{len(states)}/50 States Guessed correctly", prompt="What is another State's name? ").title()
    if answer_state in states_list:
        game_brain.play_game(data, answer_state, states)

    if answer_state=="Exit":
        game_brain.exit_game(states_list, states, empty_states)
        game_brain.write_states(states_list, data)
        break
    


screen.mainloop()