from utils.perform_rotation import perform_rotation
from day1.utils.read_rotations import read_rotations

INITIAL_POSITION = 50

class SecretEntranceSolver:
    def __init__(self, initial_position=INITIAL_POSITION):
        self.initial_position = initial_position
        self.position = initial_position
        self.rotations = read_rotations()

    def reset(self) -> None:
        self.position = self.initial_position

    def solve_part1(self) -> int:
        """Count how many times the dial ends at position 0 after complete rotations"""
        zero_count = 0
        for rotation in self.rotations:
            self.position, _ = perform_rotation(self.position, rotation.dir, rotation.val)
            if self.position == 0:
                zero_count += 1
        return zero_count

    def solve_part2(self) -> int:
        """Count all times the dial passes through position 0, including intermediate positions"""
        zero_count = 0
        for rotation in self.rotations:
            self.position, zero_passes = perform_rotation(self.position, rotation.dir, rotation.val)
            zero_count += zero_passes
        return zero_count

if __name__ == '__main__':
    solver = SecretEntranceSolver()
    print(f"Part 1 Answer: {solver.solve_part1()}")

    solver.reset()
    print(f"Part 2 Answer: {solver.solve_part2()}")
