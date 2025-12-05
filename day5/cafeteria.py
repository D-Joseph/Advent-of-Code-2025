from utils.read_data import read_data


class CafeteriaResolver:
    def __init__(self):
        self.fresh_ranges, self.ingredients = read_data()
    
    def print_data(self) -> str:
        return f'Ranges: {self.fresh_ranges}\n', f'Ingredients: {self.ingredients}'

    def solve_part1(self) -> int:
        fresh_ingredients = 0
        ingr_idx = 0
        for fresh_range in self.fresh_ranges:
            while ingr_idx < len(self.ingredients):
                curr_ingr = self.ingredients[ingr_idx]
                if curr_ingr < fresh_range.start:
                    ingr_idx += 1
                    continue
                elif curr_ingr > fresh_range.end:
                    break
                else:
                    fresh_ingredients += 1
                    ingr_idx += 1
        return fresh_ingredients


    def solve_part2(self) -> int:
        pass


if __name__ == '__main__':
    solver = CafeteriaResolver()
    print(solver.print_data())
    print(f"Part 1 Answer: {solver.solve_part1()}")
    print(f"Part 2 Answer: {solver.solve_part2()}")
