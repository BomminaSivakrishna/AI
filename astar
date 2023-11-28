import heapq
import copy

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

def print_puzzle(puzzle):
    for row in puzzle:
        print(" ".join(map(str, row)))

def find_blank(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i, j

def is_goal(state, goal_state):
    return state == goal_state

def manhattan_distance(state, goal_state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_row, goal_col = divmod(value - 1, 3)
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance

def get_neighbors(state):
    i, j = find_blank(state)
    neighbors = []

    if i > 0:
        up_neighbor = copy.deepcopy(state)
        up_neighbor[i][j], up_neighbor[i - 1][j] = up_neighbor[i - 1][j], up_neighbor[i][j]
        neighbors.append(up_neighbor)

    if i < 2:
        down_neighbor = copy.deepcopy(state)
        down_neighbor[i][j], down_neighbor[i + 1][j] = down_neighbor[i + 1][j], down_neighbor[i][j]
        neighbors.append(down_neighbor)

    if j > 0:
        left_neighbor = copy.deepcopy(state)
        left_neighbor[i][j], left_neighbor[i][j - 1] = left_neighbor[i][j - 1], left_neighbor[i][j]
        neighbors.append(left_neighbor)

    if j < 2:
        right_neighbor = copy.deepcopy(state)
        right_neighbor[i][j], right_neighbor[i][j + 1] = right_neighbor[i][j + 1], right_neighbor[i][j]
        neighbors.append(right_neighbor)

    return neighbors

def astar_search(initial_state, goal_state):
    open_set = []
    closed_set = set()

    initial_node = Node(initial_state)
    heapq.heappush(open_set, initial_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if is_goal(current_node.state, goal_state):
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(tuple(map(tuple, current_node.state)))

        for neighbor_state in get_neighbors(current_node.state):
            if tuple(map(tuple, neighbor_state)) in closed_set:
                continue

            g_score = current_node.g + 1
            h_score = manhattan_distance(neighbor_state, goal_state)
            neighbor_node = Node(neighbor_state, current_node, g_score, h_score)

            if neighbor_node not in open_set:
                heapq.heappush(open_set, neighbor_node)

    return None

def input_puzzle(prompt):
    print(prompt)
    puzzle = []
    for i in range(3):
        row = list(map(int, input().split()))
        puzzle.append(row)
    return puzzle

if __name__ == "__main__":
    print("Enter the initial state (3x3 puzzle, use 0 for the blank tile):")
    initial_state = input_puzzle("")

    print("Enter the goal state (3x3 puzzle, use 0 for the blank tile):")
    goal_state = input_puzzle("")

    path = astar_search(initial_state, goal_state)

    if path:
        print("Solution found:")
        for step, state in enumerate(path):
            print(f"Step {step + 1}:")
            print_puzzle(state)
    else:
        print("No solution found.")
