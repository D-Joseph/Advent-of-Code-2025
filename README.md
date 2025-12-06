# Advent of Code 2025

Python implementations for each day's puzzle. Every day directory contains:

- Solver code (`dayN/<theme>.py`) plus helper utilities.
- Puzzle summary and solution write-up (`dayN/dayN.md`) that removes the original answers.
- Sample input file (`dayN/*_input.txt`) matching the structure of the official puzzle input.

## Repository Layout

- `day1/`: Dial rotations puzzle (`secret_entrance.py`).
- `day2/`: Gift shop ID ranges (`gift_shop.py`).
- `day3/`: Lobby battery banks (`lobby.py`).
- `day4/`: Printing department forklift access (`printing_dept.py`).
- `day5/`: Cafeteria ingredient ranges (`cafeteria.py`).

Each `dayN.md` outlines the puzzle goals and describes how the Python solution works. Utilities live under `dayN/utils/`.

## Running a Solver

Use Python 3.11+:

```bash
python dayN/<theme>.py
```

Replace `N` and `<theme>` with the desired day. Solvers read their accompanying `*_input.txt` files by default; edit those files or adjust the helper functions if you want to test alternate inputs.
