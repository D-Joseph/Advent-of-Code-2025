# Day 2 Problem

You are given ranges of product IDs from the North Pole gift shop database. Each ID is a positive integer without leading zeroes. Some IDs are invalid because their digits form a smaller sequence that is repeated back-to-back; the task is to find every invalid ID inside the provided ranges and add them together.

## Part 1

An ID is invalid only when it is exactly two repeats of the same digit sequence (e.g., `123123`). For every range in the input, identify all IDs that match this pattern and compute the total sum of those invalid values.

### Solution Explanation

For each numeric range, the solver constructs candidate IDs by taking the first half of a possible ID, duplicating it, and checking whether the result falls within the current bounds. `next_multiple_10` is used to jump to the next range boundary that guarantees an even number of digits, since only even-length IDs can be formed from two repeats. `count_invalid_in_range` then walks forward through all candidates, accumulates the values that stay within the range, and uses a `seen` set to prevent double-counting when ranges overlap.

## Part 2

Now an ID is invalid if its digits consist of any sequence repeated at least twice (e.g., `12` repeated five times to make `1212121212`). Using the same ranges, find the sum of all IDs that match this broader rule.

### Solution Explanation

The solver extends the Part 1 approach by considering multiple split sizes—2, 3, 5, and 7—to represent the possible counts of repeated segments in the puzzle input. For each split that evenly divides the current digit length, it generates candidates via `count_invalid_in_range`. When a range crosses into IDs with a different number-of-digits parity, `next_multiple_10` is used to restart the search at the next threshold so the solver can repeat the process for the new length class. All matching IDs are summed while continuing to guard against double-counting.

