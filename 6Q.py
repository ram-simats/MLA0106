# Vacuum Cleaner Problem

def vacuum_agent(location, state):
    """
    location : 'A' or 'B'
    state : {'A': 'Clean/Dirty', 'B': 'Clean/Dirty'}
    """

    if state[location] == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    else:
        return "Left"


def run_vacuum(state, start_location):
    location = start_location
    steps = 0

    print("Initial State:", state)
    print("Starting Location:", location)
    print("--------------------------------")

    while state["A"] == "Dirty" or state["B"] == "Dirty":

        action = vacuum_agent(location, state)
        print(f"Vacuum at {location} → Action: {action}")

        if action == "Suck":
            state[location] = "Clean"
        elif action == "Right":
            location = "B"
        elif action == "Left":
            location = "A"

        steps += 1

    print("--------------------------------")
    print("Final State:", state)
    print("Goal Achieved in", steps, "steps")


# Example Input
environment = {
    "A": "Dirty",
    "B": "Dirty"
}

run_vacuum(environment, "A")
