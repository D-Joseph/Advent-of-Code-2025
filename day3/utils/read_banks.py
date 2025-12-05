from typing import List


def read_banks(path: str = './lobby_input.txt') -> List[str]:
    banks: List[str] = []
    with open(path, 'r') as file:
        for line in file:
            banks.append(line.strip())
    return banks
