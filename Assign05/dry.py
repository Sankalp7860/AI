from queue import PriorityQueue

def generate_all_possible_actions(state):
    possible_actions = []
    missionaries, cannibals, boat_position = state
    for move_m, move_c in [(0,1), (0,2), (1,0), (1,1), (2,0)]:
        if boat_position == 1:
            move_m, move_c = -move_m, -move_c
        new_state = (missionaries + move_m, cannibals + move_c, boat_position ^ 1)
        if is_state_valid(new_state):
            cost = 10 * abs(move_m) + 20 * abs(move_c)
            possible_actions.append((new_state, cost))
    return possible_actions

def is_state_valid(state):
    missionaries, cannibals, boat_position = state
    return 0 <= missionaries <= 3 and 0 <= cannibals <= 3 and (missionaries == 0 or missionaries >= cannibals) and (missionaries == 3 or missionaries <= cannibals)

def find_optimal_path():
    initial_state = ((3, 3, 1), 0)
    goal_state = (0, 0, 0)
    priority_queue = PriorityQueue()
    priority_queue.put((0, [initial_state]))
    visited_states = set()
    while not priority_queue.empty():
        total_cost, path = priority_queue.get()
        state = path[-1][0]
        if state == goal_state:
            return total_cost, path
        visited_states.add(state)
        for action in generate_all_possible_actions(state):
            new_state, action_cost = action
            if new_state not in visited_states:
                new_total_cost = total_cost + action_cost
                new_path = path + [(new_state, action_cost)]
                priority_queue.put((new_total_cost, new_path))
    return -1, []

def print_output(total_cost, path):
    print("\tBoat Transportation Simulation:")
    print("\nAssuming the boat cannot go empty from any side...")
    for state, current_cost in path:
        missionaries, cannibals, boat_position = state
        missionaries_on_other_side = abs(3 - missionaries)
        cannibals_on_other_side = abs(3 - cannibals)
        print("\nOriginal Side: (" + str(missionaries) + ", " + str(cannibals) + ")")
        print(" Opposite Side: (" + str(missionaries_on_other_side) + ", " + str(cannibals_on_other_side) + ")")
        print("Boat Position (0: on the opposite side, 1: on the original side): " + str(boat_position))
        print("Cost: " + str(current_cost))
    print("\nTotal Cost: Rs %d" % total_cost)

def main():
    total_cost, path = find_optimal_path()
    print_output(total_cost, path)

if __name__ == "__main__":
    main()