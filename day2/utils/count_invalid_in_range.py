def count_invalid_in_range(gift_range, initial, splits, seen):
    start, end = gift_range.start, gift_range.end
    invalid_count = 0
    identifier = initial[: len(initial) // splits]

    # Protect against starting with an id outside of the range
    while int(identifier * splits) < int(start):
        identifier = str(int(identifier) + 1)

    while int(identifier * splits) <= int(end):
        value = int(identifier * splits)
        if value not in seen:
            invalid_count += value
            seen.add(value)
        identifier = str(int(identifier) + 1)

    return invalid_count
