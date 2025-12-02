from utils.rotation import Rotation
from typing import List

def read_rotations(input_path: str = './secret_entrance_input.txt') -> List[Rotation]:
        rotations = []
        with open(input_path, 'r') as file:
            for line in file:
                rotations.append(Rotation(line[0], int(line[1:])))
        return rotations