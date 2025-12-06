# Day 5 Problem

The cafeteria database lists inclusive ranges of fresh ingredient IDs, a blank line, and then a list of available ingredient IDs. Ranges may overlap, and any ID present in at least one range is considered fresh. Part 1 asks how many of the listed available IDs are fresh; Part 2 asks how many total IDs fall within the union of all ranges.

## Part 1

Given the ordered ranges and sorted ingredient list, count how many ingredient IDs fall inside any fresh range.

### Solution Explanation

`read_data` parses both the ranges and the ingredient IDs, sorting each list. During part 1, the solver walks the ranges sequentially and advances a pointer over the ingredient list. For each range, it skips ingredients that are below the start, counts ingredients that fall inside the range, and stops when the current ingredient exceeds the end. This two-pointer pass avoids repeatedly scanning the full list.

## Part 2

Ignore the explicit ingredient list and instead compute the size of the union of all ranges, counting every ID covered by at least one range.

### Solution Explanation

`combine_ranges` merges overlapping or adjacent `IDRange` objects by scanning the sorted ranges, extending the current range whenever the next range starts before the current one ends. After merging, the solver simply sums `end - start + 1` for each combined range to get the total number of fresh IDs.

