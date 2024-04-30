from typing import Literal


class Adventurer:
    """Adventurer tracks its location with lat & lng. Positive lat is north, negative is south. Positive lng is east, negative is west"""

    def __init__(self):
        self.lat = 0
        self.lng = 0

    def move(self, steps: int, direction: Literal["F", "B", "R", "L"]):
        match direction:
            case "F":
                self.lat += steps
            case "B":
                self.lat -= steps
            case "R":
                self.lng += steps
            case "L":
                self.lng -= steps
