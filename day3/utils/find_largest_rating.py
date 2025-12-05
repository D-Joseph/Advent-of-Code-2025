from typing import Tuple

def find_largest_rating(bank: str, start: int, end: int) ->  Tuple[int, int]:
    maxVal = int(bank[start])
    maxValIdx = start
    for i in range(start, end):
        battery = int(bank[i])
        if  battery > maxVal:
            maxVal = battery
            maxValIdx = i
    return maxVal, maxValIdx

