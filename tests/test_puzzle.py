import pytest
from puzzle15.puzzle import Puzzle

def test_puzzle_initialization():
    # Test valid puzzle initialization
    with pytest.raises(ValueError):
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, -1]]
        puzzle = Puzzle(grid)

    # Test invalid puzzle with duplicates
    with pytest.raises(ValueError):
        Puzzle([[1, 1, 3], [4, 5, 6], [7, 8, -1]])

    # Test invalid puzzle with missing blank
    with pytest.raises(ValueError):
        Puzzle([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def test_puzzle_from_dimensions():
    # Test 3x3 puzzle generation
    puzzle = Puzzle.from_dimensions(3, 3)
    assert puzzle.height == 3
    assert puzzle.width == 3
    assert puzzle.is_solvable()

    # Test 4x4 puzzle generation
    puzzle = Puzzle.from_dimensions(4, 4)
    assert puzzle.height == 4
    assert puzzle.width == 4
    assert puzzle.is_solvable()

def test_puzzle_from_string():
    # Test valid puzzle string
    puzzle_str = "1 2 3|4 5 6|7 8 -1"
    puzzle = Puzzle.from_string(puzzle_str)
    assert puzzle.height == 3
    assert puzzle.width == 3
    assert puzzle.blank_pos == (2, 2)

    # Test invalid puzzle string (not solvable)
    with pytest.raises(ValueError):
        Puzzle.from_string("2 1 3|4 5 6|7 8 -1")

def test_is_solvable():
    # Test solvable puzzle
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, -1]]
    puzzle = Puzzle(grid)
    assert puzzle.is_solvable()

    # Test unsolvable puzzle
    grid = [[2, 1, 3], [4, 5, 6], [7, 8, -1]]
    puzzle = Puzzle(grid)
    assert not puzzle.is_solvable()        

def test_possible_moves():
    # Test moves in center position
    grid = [[1, 2, 3], [4, -1, 6], [7, 8, 5]]
    puzzle = Puzzle(grid)
    moves = puzzle.possible_moves()
    assert set(moves) == {'up', 'down', 'left', 'right'}

    # Test moves in corner position
    grid = [[-1, 2, 3], [4, 5, 6], [7, 8, 1]]
    puzzle = Puzzle(grid)
    moves = puzzle.possible_moves()
    assert set(moves) == {'down', 'right'}

def test_move():
    # Test valid move
    grid = [[1, 2, 3], [4, -1, 6], [7, 8, 5]]
    puzzle = Puzzle(grid)
    puzzle.move('right')
    assert puzzle.grid[1][2] == -1
    assert puzzle.grid[1][1] == 6

    # Test invalid move
    grid = [[-1, 2, 3], [4, 1, 6], [7, 8, 5]]
    puzzle = Puzzle(grid)
    with pytest.raises(ValueError):
        puzzle.move('up')

def test_grid(self):
    # Create a puzzle with a known grid
    initial_grid = [
        [1, 2, 3],
        [4, -1, 5],
        [6, 7, 8]
    ]
    puzzle = Puzzle(initial_grid)
    
    # Get the grid copy
    grid_copy = puzzle.grid()
    
    self.assertIsNot(grid_copy, puzzle.grid)
    self.assertEqual(grid_copy, initial_grid)
    
    # Modify the copy and verify original is unchanged
    grid_copy[0][0] = 999
    self.assertEqual(puzzle.grid, initial_grid)

def test_is_solved(self):
    solved_grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, -1]
    ]
    puzzle = Puzzle(solved_grid)
    self.assertTrue(puzzle.is_solved())

    unsolved_grid = [
        [1, 2, 3],
        [4, -1, 5],
        [6, 7, 8]
    ]
    puzzle = Puzzle(unsolved_grid)
    self.assertFalse(puzzle.is_solved())