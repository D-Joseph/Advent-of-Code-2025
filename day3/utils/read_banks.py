def read_banks(path='./lobby_input.txt'):
    banks = []
    with open(path, 'r') as file:
        for line in file:
            banks.append(line.strip())
    return banks