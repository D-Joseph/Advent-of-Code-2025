from utils.read_banks import read_banks
class LobbyResolver:
    def __init__(self):
        self.banks = read_banks()
    
    def solve_part1(self):
        joltage_sum = 0
        for bank in self.banks:
            maxTens = 0
            maxTensIdx = 0
            for i in range(len(bank) - 1):
                if int(bank[i]) > maxTens:
                    maxTens = int(bank[i])
                    maxTensIdx = i

            maxOnes = 0
            for i in range(maxTensIdx+1, len(bank)):
                maxOnes = max(maxOnes, int(bank[i]))
            
            joltage_sum += (maxTens * 10 + maxOnes)
        return joltage_sum
            


    def print_banks(self):
        for bank in self.banks:
            print(bank)

if __name__ == '__main__':
    solver = LobbyResolver()
    print(f"Part 1 Answer: {solver.solve_part1()}")
