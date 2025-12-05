from typing import List


def check_surroundings(grid: List[List[str]], row: int, col: int) -> bool:
    rolls = 0
    for row_diff in (-1, 0, 1):
        for col_diff in (-1, 0, 1):
            new_row = row + row_diff
            new_col = col + col_diff
            if row_diff == col_diff == 0:
                continue
            if (
                new_row < 0
                or new_row == len(grid)
                or new_col < 0
                or new_col == len(grid[0])
            ):
                continue
            if grid[new_row][new_col] == '@':
                rolls += 1
    return rolls < 4
