"""This file contains the TestCPU class."""
import unittest
from src.Board import Board
from src.CPU import CPU


class TestCPU(unittest.TestCase):
    """This class tests the CPU class."""
    def setUp(self):
        self.cpu_player = CPU("O", "X")

    def test_next_move_win(self):
        """Test the CPU will take the win if available."""
        board = Board(7, 7, 3)

        # Populate each board in one of the four quadrants.
        board.grid = [[".", ".", ".", ".", ".", ".", "."],
                      [".", ".", ".", ".", ".", ".", "."],
                      [".", ".", "O", ".", "O", ".", "."],
                      [".", ".", ".", "X", ".", ".", "."],
                      [".", ".", ".", ".", ".", ".", "."],
                      [".", "X", ".", ".", ".", "X", "."],
                      [".", ".", ".", ".", ".", ".", "."]]

        # This only works because the test boards are square.
        # If we omit this line, the Boards above are transposed
        # when compared to above. With this line, you can imagine
        # the list of lists above as the grid.
        board.grid = list(map(list, zip(*board.grid)))

        # Assert the CPU goes in the (4,2) position, taking the win.
        self.assertEqual(board.grid[3][2], ".", board.to_string())
        self.cpu_player.move(board)
        self.assertEqual(board.grid[3][2], "O", board.to_string())


if __name__ == "__main__":
    unittest.main()
