from collections import deque


def is_goal_state(state):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return state == goal_state


def get_next_states(state):
    next_states = []
    zero_row, zero_col = find_zero_position(state)

    if zero_row > 0:
        next_state = [row[:] for row in state]
        next_state[zero_row][zero_col], next_state[zero_row - 1][zero_col] = next_state[zero_row - 1][zero_col], next_state[zero_row][zero_col]
        next_states.append(next_state)

    if zero_row < 2:
        next_state = [row[:] for row in state]
        next_state[zero_row][zero_col], next_state[zero_row + 1][zero_col] = next_state[zero_row + 1][zero_col], next_state[zero_row][zero_col]
        next_states.append(next_state)

    if zero_col > 0:
        next_state = [row[:] for row in state]
        next_state[zero_row][zero_col], next_state[zero_row][zero_col - 1] = next_state[zero_row][zero_col - 1], next_state[zero_row][zero_col]
        next_states.append(next_state)

    if zero_col < 2:
        next_state = [row[:] for row in state]
        next_state[zero_row][zero_col], next_state[zero_row][zero_col + 1] = next_state[zero_row][zero_col + 1], next_state[zero_row][zero_col]
        next_states.append(next_state)

    return next_states

def find_zero_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def bfs_search(initial_state):
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        state, path = queue.popleft()
        visited.add(tuple(map(tuple, state)))

        if is_goal_state(state):
            return path

        for next_state in get_next_states(state):
            if tuple(map(tuple, next_state)) not in visited:
                queue.append((next_state, path + [next_state]))

    return None



initial_state = [[8,6,7], [2,5,4], [3,0,1]]
#initial_state = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
path = bfs_search(initial_state)
if path:
    print("Solution found!")
    for i in range(0,len(path)):
        for j in range(0,3):
            print(path[i][j])
        print("\n")
else:
    print("No solution found.")
print("PathLength: ", len(path))
