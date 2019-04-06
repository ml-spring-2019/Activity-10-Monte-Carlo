import random
import pdb
graph = {}

def main():

    state_num, action_num = 1, 2
    create_graph()
    ending_states = transition(state_num, action_num)
    print(generate_episode("state_1"))


def create_graph():
    global graph
    graph['state_1'] = {"action_1": ("state_2",), "action_2": ("state_3", "state_5")}
    graph['state_2'] = {"action_1": ("state_4",), "action_2": ("state_1", "state_4")}
    graph['state_3'] = {"action_1": ("state_5",), "action_2": ("state_4",)}
    graph['state_4'] = {"action_1": ("state_3",), "action_2": ("state_5",)}

def transition(state_num, action_num):
    global graph
    return graph["state_" + str(state_num)]["action_" + str(action_num)]

def reward(action_state, ending_state):
    if ending_state == "state_5":
        return 20
    elif action_state == "action_1":
        return -1
    return -2

def generate_episode(start_state):
    global graph
    steps = ""
    if start_state == "state_5":
        return "state_5"

    # randomize an action and get tuple
    act_tup = transition(int(start_state[-1]), random.randint(1,2))

    for state in act_tup:
#        pdb.set_trace()
        steps = generate_episode(state)
    return start_state + " " + steps

if __name__ == "__main__":
    main()
