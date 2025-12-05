from typing import List

def read_grid(path:str='./printing_dept_input.txt'):
    with open(path, 'r') as file:
        grid: List[List[str]] = []
        for line in file:
            stripped = line.strip()
            if stripped:
                grid.append(list(stripped))
    return grid