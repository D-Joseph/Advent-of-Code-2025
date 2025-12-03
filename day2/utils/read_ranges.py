from utils.range import Range
from typing import List


def read_ranges(input_path: str = './gift_shop_input.txt') -> List[Range]:
        ranges = []
        with open(input_path, 'r') as file:
            for line in file:
                  raw = line.split(',')
                  for range in raw:
                    bounds = range.split('-')
                    ranges.append(Range(bounds[0], bounds[1]))
        return ranges