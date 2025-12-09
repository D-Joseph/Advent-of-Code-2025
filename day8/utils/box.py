from typing import Self
import math

class Box:
    def __init__(self, coords):
        self.x, self.y, self.z = [int(i) for i in coords.split(',')]
    
    def calculate_distance(self, other:Self) -> float:
        return math.sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2) + ((self.z - other.z) ** 2))
    
    def __str__(self) -> str:
        return f'({self.x}, {self.y}, {self.z})'

    def __repr__(self) -> str:
        return self.__str__()