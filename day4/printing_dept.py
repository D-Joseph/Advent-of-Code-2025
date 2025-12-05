from utils.read_grid import read_grid
from utils.check_surroundings import check_surroundings


class PrintingDeptSolver:
    def __init__(self) -> None:
        self.grid = read_grid()

    def solve_part1(self) -> int:
        rolls = 0
        for r, row in enumerate(self.grid):
            for c, item in enumerate(row):
                if item == '@' and check_surroundings(self.grid, r, c):
                    rolls += 1
        return rolls

    def solve_part2(self) -> int:
        rolls = 0
        changed = -1
        while changed != 0:
            changed = 0
            for r, row in enumerate(self.grid):
                for c, item in enumerate(row):
                    if item == '@' and check_surroundings(self.grid, r, c):
                        rolls += 1
                        changed += 1
                        self.grid[r][c] = 'x'
        return rolls


if __name__ == '__main__':
    solver = PrintingDeptSolver()
    print(f"Part 1 Answer: {solver.solve_part1()}")
    print(f"Part 2 Answer: {solver.solve_part2()}")
