from adventurer import Adventurer


def parse_directions(sequence: str):
    """Parses a directional sequence string (e.g. 12F4B for 12 steps forward, 4 back) into a list of tuples containing the number of steps as an int and the direction as a str."""

    directions = []
    steps = 0

    for char in sequence:
        try:
            num = int(char)
            if steps > 0:
                steps *= 10
            steps += num
        except ValueError:
            if char not in ["F", "B", "R", "L"]:
                print(
                    f"{char} is not a possible direction, please re-evaluate your sequence and try again."
                )
                exit()
            directions.append((steps, char))
            steps = 0

    return directions


def main():
    prompt = """Please enter a direction sequence to move your adventurer! Each instruction in the sequence starts with the number of steps followed by the direction.
    
F for forward
B for backward
R for right
L for left

Example: 5F25R15B is five steps forward, 25 steps right, 15 steps back.

> """

    direction_sequence = input(prompt)
    adventurer = Adventurer()


main()
