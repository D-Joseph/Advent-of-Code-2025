from utils.read_ranges import read_ranges
from utils.range import Range
from typing import List

class GiftShopResolver:
    def __init__(self, ranges: List[Range]):
        self.ranges = ranges
    
    def solve_part1(self):
        for range in self.ranges:
            print(range)

if __name__ == '__main__':
    solver = GiftShopResolver(read_ranges())
    print(f"Part 1 Answer: {solver.solve_part1()}")



