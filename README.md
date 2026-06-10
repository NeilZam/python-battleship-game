# Python Battleship Game

A terminal-based Battleship game written in Python. The program randomly places 8 ships on a 10x10 grid and gives the player 50 shots to sink them all. Ships are placed in random directions and sizes, and the game tracks hits, misses, and fully sunk ships in real time.

---

## How It Works

At the start of each game the board is randomly generated — 8 ships of size 3 to 5 are placed in random directions (up, down, left, right) with collision detection preventing overlaps. The player enters a row letter and column number to fire a shot. The board updates after each shot showing hits (X), misses (#), and remaining ship cells (hidden by default). The game ends when all ships are sunk or the player runs out of shots.

---

## Getting Started

### Prerequisites

- Python 3.x

### Run

```bash
python3 battleship.py
```

No external libraries required — uses only Python's built-in `random` and `time` modules.

---

## How to Play

- Enter a coordinate like `A3` or `J9` to fire a shot
- Row is a letter from A to J, column is a number from 0 to 9
- The board shows your previous shots after each turn
- Sink all 8 ships before running out of bullets to win

**Board symbols:**

| Symbol | Meaning |
|---|---|
| `.` | Unshot water |
| `O` | Ship (hidden in normal mode) |
| `X` | Hit |
| `#` | Miss |

---

## Sample Output

```
-----Welcome to Battleships-----
You have 50 bullets to take down 8 ships, may the battle begin!

A) . . . . . . . . . .
B) . . . . . . . . . .
C) . . . . . . . . . .
...
  0 1 2 3 4 5 6 7 8 9

Number of ships remaining: 8
Number of bullets left: 50
Enter row (A-J) and column (0-9) such as A3: C4

----------------------------
You hit! A ship was shot
----------------------------
```

---

## Features

- 10x10 randomized game board generated fresh each session
- 8 ships placed with random size (3 to 5 cells) and random direction
- Collision detection prevents ships from overlapping
- Full input validation with descriptive error messages
- Tracks hits, misses, and fully sunk ships separately
- Win condition triggers when all ships are sunk
- Loss condition triggers when shots are exhausted
- Debug mode toggle to reveal ship positions during development

---

## Concepts Used

- 2D list grid logic
- Randomization and seeding
- Input validation and error handling
- Game loop design
- Modular function design

---

## Technologies

- Python 3
- Standard Library only (random, time)
- Terminal / Command Line

---

## What I Learned

This project strengthened my understanding of 2D array manipulation, randomized grid generation, and designing a clean game loop. Implementing the ship sinking check — verifying that every cell of a ship had been hit before declaring it sunk — was a key challenge that reinforced my approach to boundary checking and state tracking.
