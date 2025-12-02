# Day 1 Problem

You are given a circular dial labeled with the numbers 0 through 99. The dial always begins pointing at position 50.

You also receive a sequence of rotation instructions. Each instruction consists of:

- A direction
    - L for rotating left (toward decreasing numbers)
    - R for rotating right (toward increasing numbers)

- A positive integer indicating how many clicks the dial should move (each click advances the dial by 1 position)

The dial wraps around: moving left from 0 results in 99, and moving right from 99 results in 0.

## Part 1

Simulate each rotation in order. After each full rotation is completed, note the dial’s resulting position.

Your task is to count how many times the dial ends a rotation at position 0, starting from the initial value of 50.

### Solution Explanation

The solution simulates each rotation in sequence, tracking the dial position after each complete rotation. Starting at position 50, for each rotation instruction:
- Left rotations (L) are converted to negative values
- Right rotations (R) remain positive
- The new position is calculated using modulo 100 to handle wrapping (0-99 range)
- After each complete rotation, we check if the final position equals 0

This approach only counts when the dial lands exactly on 0 after completing a full rotation.

## Part 2

Simulate the same rotations, but count every time the dial points at 0, including:

Intermediate positions encountered during the click-by-click movement of a rotation
    - Ending positions after a rotation completes
    - Large rotation values may cause the dial to pass over 0 multiple times.

Your task is to count all such occurrences, still beginning from the initial dial position of 50.

### Solution Explanation

This solution builds on Part 1 but counts every pass through position 0, not just final positions. The key insights:

1. **Multiple complete wraps**: Large rotation values (e.g., 250) cause multiple full circles around the dial. We calculate `zero_passes = value // 100` to count how many complete wraps occur.

2. **Boundary crossing detection**: When moving from one position to another, we need to detect if the movement crosses through 0:
   - Moving left (negative direction) crosses 0 when the raw position goes to/below 0 (unless already at 0)
   - Moving right crosses 0 when the raw position goes to/above 100

3. **Handling the remainder**: After accounting for complete wraps, we apply `value % 100` to get the final position within the 0-99 range.

This approach ensures we count all instances where the dial points at 0 during any part of the rotation sequence.

