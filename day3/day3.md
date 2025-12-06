# Day 3 Problem

Each line of the input lists a bank of battery ratings as digits 1-9. To power the lobby escalator, you must pick specific batteries from each bank, keeping their original order, to form a number. The goal is to maximize the per-bank output and sum these maximums across all banks.

## Part 1

Select exactly two batteries from every bank to form the highest possible two-digit value (e.g., choosing digits `9` then `8` forms `98`). Compute the total output by summing those best two-digit numbers across all banks.

### Solution Explanation

For every bank string, the solver scans for the highest digit to place in the tens position, remembers its index, then searches the remaining suffix for the best digit to place in the ones slot. This greedy pick works because only two digits are required and their relative order must remain unchanged. Each per-bank maximum is added to a running total.

## Part 2

Now you must enable exactly twelve batteries in each bank, again preserving order, to form the largest possible 12-digit number. The final answer is the sum of these per-bank maxima.

### Solution Explanation

The solver repeats the greedy idea but for twelve digits: for each position `i` (0–11), it scans the remaining digits to find the highest value that still leaves enough characters to fill the remaining slots. Once a digit is chosen, the search window advances to start after that digit. By multiplying each chosen digit by its positional power of ten and accumulating the results, the algorithm produces the maximum possible 12-digit number for each bank and sums the totals.
