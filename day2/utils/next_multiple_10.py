def next_multiple_10(num: str, evenOutput: bool):
    if (evenOutput and len(num) % 2 != 0) or (not evenOutput and len(num) % 2 == 0): 
        return '1' + '0' * len(num)
    return num
    