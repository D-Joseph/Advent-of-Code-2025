from typing import Tuple


def find_largest_rating(bank: str, start: int, end: int) -> Tuple[int, int]:
    max_value = int(bank[start])
    max_value_idx = start
    for idx in range(start, end):
        battery = int(bank[idx])
        if battery > max_value:
            max_value = battery
            max_value_idx = idx
    return max_value, max_value_idx
