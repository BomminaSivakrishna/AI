class State:
    def __init__(self, monkey_position, box_position, banana_position, on_box):
        self.monkey_position = monkey_position
        self.box_position = box_position
        self.banana_position = banana_position
        self.on_box = on_box

    def __eq__(self, other):
        return (
            self.monkey_position == other.monkey_position
            and self.box_position == other.box_position
            and self.banana_position == other.banana_position
            and self.on_box == other.on_box
        )

    def __hash__(self):
        return hash(
            (
                self.monkey_position,
                self.box_position,
                self.banana_position,
                self.on_box,
            )
        )

def monkey_banana_problem(initial_state, goal_state):
    visited = set()
    stack = [([], initial_state)]

    while stack:
        actions, current_state = stack.pop()

        if current_state == goal_state:
            return actions

        visited.add(current_state)

        if current_state.monkey_position == "left":
            new_state = State(
                "right",
                current_state.box_position,
                current_state.banana_position,
                current_state.on_box,
            )
            if new_state not in visited:
                stack.append((actions + ["Move right"], new_state))

            if current_state.on_box:
                new_state = State(
                    "right",
                    current_state.box_position,
                    current_state.banana_position,
                    False,
                )
                if new_state not in visited:
                    stack.append((actions + ["Climb onto the box"], new_state))

        elif current_state.monkey_position == "right":
            new_state = State(
                "left",
                current_state.box_position,
                current_state.banana_position,
                current_state.on_box,
            )
            if new_state not in visited:
                stack.append((actions + ["Move left"], new_state))

            if current_state.on_box:
                new_state = State(
                    "left",
                    current_state.box_position,
                    current_state.banana_position,
                    False,
                )
                if new_state not in visited:
                    stack.append((actions + ["Climb onto the box"], new_state))

        if current_state.monkey_position == current_state.box_position:
            if current_state.on_box:
                new_state = State(
                    current_state.monkey_position,
                    "right",
                    current_state.banana_position,
                    True,
                )
                if new_state not in visited:
                    stack.append((actions + ["Push the box right"], new_state))
            else:
                new_state = State(
                    current_state.monkey_position,
                    "left",
                    current_state.banana_position,
                    True,
                )
                if new_state not in visited:
                    stack.append((actions + ["Push the box left"], new_state))

    return None

def main():
    try:
        monkey_position = input("Enter the initial position of the monkey (left or right): ")
        box_position = input("Enter the initial position of the box (left or right): ")
        banana_position = input("Enter the initial position of the banana (left or right): ")

        initial_state = State(monkey_position, box_position, banana_position, False)
        goal_state = State("right", "right", "right", True)

        solution = monkey_banana_problem(initial_state, goal_state)
        if solution:
            print("Solution:")
            for action in solution:
                print(action)
        else:
            print("No solution found.")
    except KeyboardInterrupt:
        print("\nOperation interrupted.")

if __name__ == "__main__":
    main()
