from typing import Literal


class Adventurer:
    """Adventurer tracks its location with lat & lng. Positive lat is north, negative is south. Positive lng is east, negative is west"""

    def __init__(self):
        self.lat = 0
        self.lng = 0

    def move(self, amount: int, direction: Literal["F", "B", "R", "L"]):
        match direction:
            case "F":
                self.lat += amount
            case "B":
                self.lat -= amount
            case "R":
                self.lng += amount
            case "L":
                self.lng -= amount
