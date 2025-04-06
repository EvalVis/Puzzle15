import random
from typing import List, Tuple

class Puzzle:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        self.blank_pos = self._find_blank()
        self._validate_puzzle()

    @classmethod
    def from_dimensions(cls, height: int, width: int):
        numbers = list(range(1, height * width)) + [-1]  # -1 denotes the blank
        random.shuffle(numbers)
        grid = [numbers[i * width:(i + 1) * width] for i in range(height)]
        puzzle = cls(grid)
        if not puzzle.is_solvable():
            puzzle._make_solvable()
        return puzzle

    @classmethod
    def from_string(cls, puzzle_str: str):
        rows = puzzle_str.strip().split('|')
        grid = [[int(cell.strip()) for cell in row.strip().split()] for row in rows]
        puzzle = cls(grid)
        if not puzzle.is_solvable():
            raise ValueError("The provided puzzle configuration is not solvable.")
        return puzzle

    def _find_blank(self) -> Tuple[int, int]:
        for i, row in enumerate(self.grid):
            for j, val in enumerate(row):
                if val == -1:
                    return i, j
        raise ValueError("No blank space (-1) found in the puzzle.")

    def _validate_puzzle(self):
        flat_list = [num for row in self.grid for num in row]
        expected_numbers = set(range(1, self.width * self.height)) | {-1}
        if set(flat_list) != expected_numbers:
            raise ValueError("Puzzle contains duplicates or incorrect numbers.")

    def is_solvable(self) -> bool:
        flat_list = [num for row in self.grid for num in row if num != -1]
        inversions = sum(
            1
            for i in range(len(flat_list))
            for j in range(i + 1, len(flat_list))
            if flat_list[i] > flat_list[j]
        )
        blank_row_from_bottom = self.height - self.blank_pos[0]

        if self.width % 2 == 1:
            return inversions % 2 == 0
        else:
            return (inversions + blank_row_from_bottom) % 2 == 1

    def _make_solvable(self):
        tiles = [(i, j) for i in range(self.height) for j in range(self.width) if self.grid[i][j] != -1]
        if len(tiles) < 2:
            raise ValueError("Not enough non-blank tiles to adjust solvability.")

        (x1, y1), (x2, y2) = tiles[0], tiles[1]
        self.grid[x1][y1], self.grid[x2][y2] = self.grid[x2][y2], self.grid[x1][y1]

    def possible_moves(self) -> List[str]:
        moves = []
        x, y = self.blank_pos
        if x > 0:
            moves.append('up')
        if x < self.height - 1:
            moves.append('down')
        if y > 0:
            moves.append('left')
        if y < self.width - 1:
            moves.append('right')
        return moves

    def move(self, direction: str):
        if direction not in self.possible_moves():
            return ValueError("Invalid move direction.")

        dx, dy = {'up': (-1, 0), 'down': (1, 0),
                  'left': (0, -1), 'right': (0, 1)}[direction]

        x, y = self.blank_pos
        nx, ny = x + dx, y + dy

        self.grid[x][y], self.grid[nx][ny] = self.grid[nx][ny], self.grid[x][y]
        self.blank_pos = (nx, ny)

    def __str__(self):
        return '\n'.join(' '.join(f"{val:2}" if val != -1 else '  ' for val in row) for row in self.grid)