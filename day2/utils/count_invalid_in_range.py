def count_invalid_in_range(range, initial, splits, seen):
    start, end = range.start, range.end
    invalid_count = 0
    id = initial[:len(initial)//splits]

    # Protect against starting with an id outside of the range
    while int(id * splits) < int(start):
        id = str(int(id) + 1)

    while int(id * splits) <= int(end):
        if (int(id * splits) not in seen):
            invalid_count += int(id*splits)
            seen.add(int(id*splits))
        id = str(int(id) + 1)

    return invalid_count