import random
import pdb
graph = {}

def main():

    state_num, action_num = 1, 2
    create_graph()
    ending_states = transition(state_num, action_num)
    result = generate_episode("state_1")
    print_result(result)

def print_result(result):
    for i in range(0, len(result)):
        dict = result[i]
        if i == len(result) - 1:
            print(dict["state"] + "(+" + str(dict["reward"]) + ")" )
        else:
            print(dict["state"] + "(" + str(dict["action"]) + ", " + str(dict["reward"]) + ")" )

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
    result = []
    if start_state == "state_5":
        return [{"state": start_state, 
                 "reward": 20}]

    # randomize an action and get tuple
    action = random.randint(1,2)
    act_tup = transition(int(start_state[-1]), action)

    #for state in act_tup:
#        pdb.set_trace()
    branch = random.randint(1, len(act_tup)) - 1
    branch_result = []
    for act in act_tup:
        dest_state = act
        if action == 1:
            my_result = [{"state": start_state, 
                          "action": action, 
                          "reward": -1}]
        elif action == 2:
            my_result = [{"state": start_state,
                          "action": action,
                          "reward": -2}]
        else:
            print("UNKNOWN ACTION " + str(action))
            exit(1)
        my_result.extend(generate_episode(dest_state))
        branch_result.append(my_result)
    if len(branch_result) == 1:
        return branch_result[0]
    else:
        # find branch with highest reward
        rewards = []
        for b in branch_result:
            my_reward = 0
            for d in b:
                my_reward += d["reward"]
            rewards.append(my_reward)
        index_of_highest_reward = rewards.index(max(rewards))
        return branch_result[index_of_highest_reward]

if __name__ == "__main__":
    main()
