def next_multiple_10(num: str, even_output: bool):
    if (even_output and len(num) % 2 != 0) or (not even_output and len(num) % 2 == 0):
        return '1' + '0' * len(num)
    return num
