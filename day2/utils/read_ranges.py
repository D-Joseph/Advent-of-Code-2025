from typing import List

from utils.range import Range


def read_ranges(input_path: str = './gift_shop_input.txt') -> List[Range]:
    ranges: List[Range] = []
    with open(input_path, 'r') as file:
        for line in file:
            raw_ranges = line.split(',')
            for raw_range in raw_ranges:
                bounds = raw_range.split('-')
                ranges.append(Range(bounds[0], bounds[1]))
    return ranges
