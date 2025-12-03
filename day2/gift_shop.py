from utils.read_ranges import read_ranges

class GiftShopResolver:
    def __init__(self):
        self.ranges = read_ranges()
    
    def solve_part1(self):
        invalid_count = 0
        for r in self.ranges:
            start = r.start

            # If the lower bound has odd digits, set it to the next even digits number
            if len(r.start) % 2 != 0:
                start = '1' + '0' * len(r.start)

            # Knowing the length of the range, we can craft invalid IDs by taking the front half of the start
            # and duplicating it, and then incrementing that front half by 1 until we reach a number larger than the end
            id = start[:len(start)//2]

            # Protect against starting with an id outside of the range
            while int(id * 2) < int(r.start):
                id = str(int(id) + 1)

            while int(id * 2) <= int(r.end):
                print(f'\t{id*2}')
                invalid_count += int(id*2)
                id = str(int(id) + 1)

        return invalid_count

    def solve_part2(self):
        invalid_count = 0
        



if __name__ == '__main__':
    solver = GiftShopResolver()
    print(f"Part 1 Answer: {solver.solve_part1()}")



