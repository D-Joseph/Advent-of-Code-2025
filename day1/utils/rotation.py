from enum import Enum

class Direction(Enum):
    LEFT = 'L'
    RIGHT = 'R'

class Rotation:
    def __init__(self, dir: str, val: int):
        self.dir = Direction(dir)
        self.val = val
    
    def __str__(self):
        return f"Direction: {self.dir}, Value: {self.val}\n"