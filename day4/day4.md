# Day 4 Problem

The printing department provides a grid of tiles where `@` represents a paper roll and `.` represents empty space. A roll is considered within reach of a forklift if fewer than four of its eight neighbors are also rolls. You must find all accessible rolls and count them.

## Part 1

Using the static grid, count every `@` tile whose surrounding eight positions include fewer than four other rolls. Report how many such rolls exist.

### Solution Explanation

The solver reads the grid into memory, then iterates over each cell. For any `@`, it calls `check_surroundings`, which inspects all eight adjacent cells (skipping bounds and the center) and counts neighboring rolls. If the count is below four, the roll contributes to the total.

## Part 2

Now rolls can be removed: once a roll is deemed accessible, it is removed, potentially exposing more rolls. Repeat the process until no additional rolls qualify, and return how many rolls were removed overall.

### Solution Explanation

Part 2 reuses `check_surroundings` but applies it iteratively. While at least one roll was removed in the previous pass, scan the grid; whenever a roll qualifies, mark it as removed (changing it from `@` to `x`) and increment the total removal count. The loop ends when a scan finds no removable rolls.

