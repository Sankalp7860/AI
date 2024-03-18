import heapq
import copy

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_row, goal_col = divmod(state[i][j] - 1, 3)
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance

class PuzzleState:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(str(self.state))

    def __lt__(self, other):
        return False  

    def is_goal(self):
        return self.state == goal_state

    def get_children(self):
        children = []
        zero_pos = self.get_zero_position()

        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for move in moves:
            new_row = zero_pos[0] + move[0]
            new_col = zero_pos[1] + move[1]

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = copy.deepcopy(self.state)
                new_state[zero_pos[0]][zero_pos[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_pos[0]][zero_pos[1]]
                children.append(PuzzleState(new_state, self, (new_row, new_col)))
        return children

    def get_zero_position(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return (i, j)

def a_star(initial_state):
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(initial_state.state), initial_state))
    closed_set = set()

    while open_list:
        _, current_state = heapq.heappop(open_list)
        if current_state.is_goal():
            return current_state

        closed_set.add(current_state)

        for child in current_state.get_children():
            if child not in closed_set:
                heapq.heappush(open_list, (child.depth + manhattan_distance(child.state), child))

def greedy(initial_state):
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(initial_state.state), initial_state))
    closed_set = set()

    while open_list:
        _, current_state = heapq.heappop(open_list)
        if current_state.is_goal():
            return current_state

        closed_set.add(current_state)

        for child in current_state.get_children():
            if child not in closed_set:
                heapq.heappush(open_list, (manhattan_distance(child.state), child))

def print_steps(solution):
    if solution is None:
        print("No solution found.")
    else:
        print("Solution found!")
        steps = []
        while solution:
            steps.append(solution)
            solution = solution.parent

        steps.reverse()
        for step, state in enumerate(steps):
            print(f"Step {step}:")
            for row in state.state:
                print(row)
            print()

initial_state = PuzzleState([[1, 2, 3], [4, 0, 5], [6, 7, 8]])

solution_a_star = a_star(initial_state)
print("A* Search:")
print_steps(solution_a_star)

solution_greedy = greedy(initial_state)
print("Greedy Best-First Search :")
print_steps(solution_greedy)

