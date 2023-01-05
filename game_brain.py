from turtle import Turtle

class GameBrain(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def play_game(self, data, answer_state, states):
        state_data=data[data.state==answer_state]
        self.goto(int(state_data.x), int(state_data.y))
        self.write(answer_state)
        states.append(answer_state)

    def exit_game(self, states_list, states, empty_states):
        for state in states_list:
            if state not in states:
                empty_states.append(state)
        print(empty_states)

    def write_states(self, states_list, data):
        for state in states_list:
            state_data=data[data.state==state]
            self.goto(int(state_data.x), int(state_data.y))
            self.write(state)

