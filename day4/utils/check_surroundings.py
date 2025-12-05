from typing import List
def check_surroundings(grid: List[List[str]], row: int, col: int):
    rolls = 0
    for rDiff in [-1, 0, 1]:
        for cDiff in [-1, 0, 1]:
            if rDiff == cDiff == 0 or row+rDiff < 0 or row+rDiff==len(grid) or col+cDiff < 0 or col+cDiff==len(grid[0]):
                continue
            if grid[row+rDiff][col+cDiff] == '@':
                rolls += 1
    return rolls < 4
