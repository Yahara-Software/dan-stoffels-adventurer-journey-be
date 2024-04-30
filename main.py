from adventurer import Adventurer


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
