from utils.count_invalid_in_range import count_invalid_in_range
from utils.next_multiple_10 import next_multiple_10
from utils.read_ranges import read_ranges

class GiftShopResolver:
    def __init__(self):
        self.ranges = read_ranges()
    
    def solve_part1(self):
        invalid_count = 0
        for r in self.ranges:
            seen = set()
            start = next_multiple_10(r.start, True)

            # Knowing the length of the range, we can craft invalid IDs by taking the front half of the start
            # and duplicating it, and then incrementing that front half by 1 until we reach a number larger than the end
            invalid_count += count_invalid_in_range(r, start, 2, seen)

        return invalid_count

    def solve_part2(self):
        invalid_count = 0
        for r in self.ranges:
            isStartEven = len(r.start) % 2 == 0
            isEndEven = len(r.end) % 2 == 0
            # First cover even -> even and odd -> odd ranges
            invalid_count += self.try_splits(r, r.start)

            # Handle when end parity is different from start
            if isStartEven != isEndEven:
                new_start = next_multiple_10(r.start, not isStartEven)
                invalid_count += self.try_splits(r, new_start)
            
        return invalid_count
    
    def try_splits(self, range, start: str):
        count = 0
        seen = set()
        for split in [2, 3, 5, 7]:
            # Only count if the length of the range is a multiple of the split
            if len(start) % split != 0:
                continue
            count += count_invalid_in_range(range, start, split, seen)
        return count
        

    def print_ranges(self):
        print("Ranges: ", end="")
        for range in self.ranges:
            print('[', range, end=" ], ")
        print("\n")

if __name__ == '__main__':
    solver = GiftShopResolver()
    print(f"Part 1 Answer: {solver.solve_part1()}")
    print(f"Part 2 Answer: {solver.solve_part2()}")



