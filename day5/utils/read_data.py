from typing import List
from utils.id_range import IDRange

def read_data(path='./cafeteria_input.txt'):
    ranges: List[IDRange] = []
    ingredients: List[str] = []
    is_populating_ranges = True
    with open(path, 'r') as file:
        for line in file:
            stripped = line.strip()
            if not stripped:
                is_populating_ranges = False
                continue
            if is_populating_ranges:
                start, end = stripped.split('-')
                ranges.append(IDRange(int(start), int(end)))
            else:
                ingredients.append(int(stripped))

    ranges.sort(key=lambda x: x.start)
    ingredients.sort(key=lambda x: int(x))
    return ranges, ingredients