from utils.find_largest_rating import find_largest_rating
from utils.read_banks import read_banks


class LobbyResolver:
    def __init__(self) -> None:
        self.banks = read_banks()

    def solve_part1(self) -> int:
        joltage_sum = 0
        for bank in self.banks:
            max_tens, max_tens_idx = find_largest_rating(bank, 0, len(bank) - 1)
            max_ones, _ = find_largest_rating(bank, max_tens_idx + 1, len(bank))
            joltage_sum += max_tens * 10 + max_ones
        return joltage_sum

    def solve_part2(self) -> int:
        joltage_sum = 0
        for bank in self.banks:
            last_idx = -1
            for i in range(12):
                max_value, last_idx = find_largest_rating(
                    bank,
                    last_idx + 1,
                    len(bank) - (12 - i - 1),
                )
                joltage_sum += max_value * (10 ** (12 - i - 1))
        return joltage_sum



if __name__ == '__main__':
    solver = LobbyResolver()
    print(f"Part 1 Answer: {solver.solve_part1()}")
    print(f"Part 2 Answer: {solver.solve_part2()}")
