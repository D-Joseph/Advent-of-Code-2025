from utils.find_largest_rating import find_largest_rating
from utils.read_banks import read_banks
class LobbyResolver:
    def __init__(self):
        self.banks = read_banks()
    
    def solve_part1(self):
        joltage_sum = 0
        for bank in self.banks:
            maxTens, maxTensIdx = find_largest_rating(bank, 0, len(bank)-1)
            maxOnes, _ = find_largest_rating(bank, maxTensIdx + 1, len(bank))
            joltage_sum += (maxTens * 10 + maxOnes)
        return joltage_sum
            
    def solve_part2(self):
        joltage_sum = 0
        for bank in self.banks:
            last_idx = 0
            for i in range(12):
                maxVal, last_idx = find_largest_rating(bank, last_idx, len(bank) - (12 - i - 1))
                joltage_sum += (maxVal * (10 * (12 - i - 1)))
        return joltage_sum

                


        
if __name__ == '__main__':
    solver = LobbyResolver()
    print(f"Part 1 Answer: {solver.solve_part1()}")
    print(f"Part 2 Answer: {solver.solve_part2()}")
