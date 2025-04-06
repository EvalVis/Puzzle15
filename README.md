# Puzzle15

15 Puzzle lib to make NxM - 1 puzzles.

## Example usage:
```python
from puzzle15.puzzle import Puzzle

p1 = Puzzle.from_dimensions(3, 4)
print("Random Puzzle:\n", p1)
print("Possible moves:", p1.possible_moves())

p2 = Puzzle.from_string("1 3 5 | 4 2 -1")
print("\nFrom String:\n", p2)
print("Possible moves:", p2.possible_moves())
```