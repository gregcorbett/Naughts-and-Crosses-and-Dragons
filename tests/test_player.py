"""This file contains the TestPlayer class."""
import unittest
from src.Board import Board
from src.Player import Player


class TestPlayer(unittest.TestCase):
    """This class tests the Player class."""
    def setUp(self):
        self.player = Player("O")

    def test_win_horizontal(self):
        """Test that a horizontal win is detected."""
        # Create 4 empty Boards to test wins in each of the four quadrants.
        board1 = Board(7, 7, 3)
        board2 = Board(7, 7, 3)
        board3 = Board(7, 7, 3)
        board4 = Board(7, 7, 3)

        # Populate each board in one of the four quadrants.
        board1.grid = [[".", "O", ".", ".", ".", "O", "."],
                       ["O", "O", "O", ".", ".", "O", "O"],
                       [".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       ["O", "O", ".", ".", ".", "O", "O"],
                       [".", "O", ".", ".", ".", "O", "."]]

        board2.grid = [[".", "O", ".", ".", ".", "O", "."],
                       ["O", "O", ".", ".", "O", "O", "O"],
                       [".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       ["O", "O", ".", ".", ".", "O", "O"],
                       [".", "O", ".", ".", ".", "O", "."]]

        board3.grid = [[".", "O", ".", ".", ".", "O", "."],
                       ["O", "O", ".", ".", ".", "O", "O"],
                       [".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       ["O", "O", ".", ".", "O", "O", "O"],
                       [".", "O", ".", ".", ".", "O", "."]]

        board4.grid = [[".", "O", ".", ".", ".", "O", "."],
                       ["O", "O", ".", ".", ".", "O", "O"],
                       [".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       ["O", "O", "O", ".", ".", "O", "O"],
                       [".", "O", ".", ".", ".", "O", "."]]

        # For each testing board above.
        for board in [board1, board2, board3, board4]:

            # This only works because the test boards are square.
            # If we omit this line, the Boards above are transposed
            # when compared to above. With this line, you can imagine
            # the list of lists above as the grid.
            board.grid = list(map(list, zip(*board.grid)))

            # Assert the helper method for detecting horizontal runs
            # of the same symbol detects the winning horizontal run.
            self.assertEqual(
                self.player.max_in_row(board, self.player.marker),
                board.win_condition,
                board.to_string()
            )

            # Assert the helper method for detecting horizontal wins
            # detects the horizontal win.
            self.assertTrue(
                self.player.win_horizontal(board, self.player.marker),
                board.to_string()
            )

            # Assert the overall win method detects a win
            self.assertTrue(
                self.player.have_i_won(board), board.to_string()
            )

    def test_win_veritcal(self):
        """Test that a vertical win is detected."""
        # Create 4 empty Boards to test wins in each of the four quadrants.
        board1 = Board(7, 7, 3)
        board2 = Board(7, 7, 3)
        board3 = Board(7, 7, 3)
        board4 = Board(7, 7, 3)

        # Populate each board in one of the four quadrants.
        board1.grid = [[".", "O", ".", ".", ".", "O", "."],
                       ["O", "O", ".", ".", ".", "O", "O"],
                       [".", "O", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       ["O", "O", ".", ".", ".", "O", "O"],
                       [".", "O", ".", ".", ".", "O", "."]]

        board2.grid = [[".", "O", ".", ".", ".", "O", "."],
                       ["O", "O", ".", ".", ".", "O", "O"],
                       [".", ".", ".", ".", ".", "O", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       ["O", "O", ".", ".", ".", "O", "O"],
                       [".", "O", ".", ".", ".", "O", "."]]

        board3.grid = [[".", "O", ".", ".", ".", "O", "."],
                       ["O", "O", ".", ".", ".", "O", "O"],
                       [".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", "O", "."],
                       ["O", "O", ".", ".", ".", "O", "O"],
                       [".", "O", ".", ".", ".", "O", "."]]

        board4.grid = [[".", "O", ".", ".", ".", "O", "."],
                       ["O", "O", ".", ".", ".", "O", "O"],
                       [".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       [".", "O", ".", ".", ".", ".", "."],
                       ["O", "O", ".", ".", ".", "O", "O"],
                       [".", "O", ".", ".", ".", "O", "."]]

        # For each testing board above.
        for board in [board1, board2, board3, board4]:

            # This only works because the test boards are square.
            # If we omit this line, the Boards above are transposed
            # when compared to above. With this line, you can imagine
            # the list of lists above as the grid.
            board.grid = list(map(list, zip(*board.grid)))

            # Assert the helper method for detecting vertical runs
            # of the same symbol detects the winning vertical run.
            self.assertEqual(
                self.player.max_in_column(board, self.player.marker),
                board.win_condition,
                board.to_string()
            )

            # Assert the helper method for detecting vertical wins
            # detects the vertical win.
            self.assertTrue(
                self.player.win_vertical(board, self.player.marker),
                board.to_string()
            )

            # Assert the overall win method detects a win
            self.assertTrue(
                self.player.have_i_won(board), board.to_string()
            )

    def test_win_nwse_diagonal(self):
        """Test that a NW/SE diagonal win is detected."""
        # Create 4 empty Boards to test wins in each of the four quadrants.
        board1 = Board(7, 7, 3)
        board2 = Board(7, 7, 3)
        board3 = Board(7, 7, 3)
        board4 = Board(7, 7, 3)

        # Populate each board in one of the four quadrants.
        board1.grid = [["O", ".", "O", ".", "O", ".", "O"],
                       [".", "O", ".", ".", ".", "O", "."],
                       [".", ".", "O", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       ["O", ".", "O", ".", "O", ".", "O"],
                       [".", "O", ".", ".", ".", "O", "."],
                       [".", ".", ".", ".", ".", ".", "."]]

        board2.grid = [["O", ".", "O", ".", "O", ".", "O"],
                       [".", "O", ".", ".", ".", "O", "."],
                       [".", ".", ".", ".", ".", ".", "O"],
                       [".", ".", ".", ".", ".", ".", "."],
                       ["O", ".", "O", ".", "O", ".", "O"],
                       [".", "O", ".", ".", ".", "O", "."],
                       [".", ".", ".", ".", ".", ".", "."]]

        board3.grid = [["O", ".", "O", ".", "O", ".", "O"],
                       [".", "O", ".", ".", ".", "O", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       ["O", ".", "O", ".", "O", ".", "O"],
                       [".", "O", ".", ".", ".", "O", "."],
                       [".", ".", ".", ".", ".", ".", "O"]]

        board4.grid = [["O", ".", "O", ".", "O", ".", "O"],
                       [".", "O", ".", ".", ".", "O", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       ["O", ".", "O", ".", "O", ".", "O"],
                       [".", "O", ".", ".", ".", "O", "."],
                       [".", ".", "O", ".", ".", ".", "."]]

        # For each testing board above.
        for board in [board1, board2, board3, board4]:

            # This only works because the test boards are square.
            # If we omit this line, the Boards above are transposed
            # when compared to above. With this line, you can imagine
            # the list of lists above as the grid.
            board.grid = list(map(list, zip(*board.grid)))

            # Assert the helper method for detecting NW/SE diagonal runs
            # of the same symbol detects the winning NW/SE diagonal run.
            self.assertEqual(
                self.player.max_in_nwse_diagonal(board,
                                                 self.player.marker),
                board.win_condition,
                board.to_string()
            )

            # Assert the helper method for detecting NW/SE diagonal wins
            # detects the NW/SE diagonal win.
            self.assertTrue(
                self.player.win_nwse_diagonal(board, self.player.marker),
                board.to_string()
            )

            # Assert the overall win method detects a win
            self.assertTrue(
                self.player.have_i_won(board), board.to_string()
            )

    def test_win_nesw_diagonal(self):
        """Test that a NE/SW diagonal win is detected."""
        # Create 4 empty Boards to test wins in each of the four quadrants.
        board1 = Board(7, 7, 3)
        board2 = Board(7, 7, 3)
        board3 = Board(7, 7, 3)
        board4 = Board(7, 7, 3)

        # Populate each board in one of the four quadrants.
        board1.grid = [["O", ".", "O", ".", "O", ".", "O"],
                       [".", "O", ".", ".", ".", "O", "."],
                       ["O", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       ["O", ".", "O", ".", "O", ".", "O"],
                       [".", "O", ".", ".", ".", "O", "."],
                       [".", ".", ".", ".", ".", ".", "."]]

        board2.grid = [["O", ".", "O", ".", "O", ".", "O"],
                       [".", "O", ".", ".", ".", "O", "."],
                       [".", ".", ".", ".", "O", ".", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       ["O", ".", "O", ".", "O", ".", "O"],
                       [".", "O", ".", ".", ".", "O", "."],
                       [".", ".", ".", ".", ".", ".", "."]]

        board3.grid = [["O", ".", "O", ".", "O", ".", "O"],
                       [".", "O", ".", ".", ".", "O", "."],
                       [".", ".", ".", ".", "O", ".", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       ["O", ".", "O", ".", "O", ".", "O"],
                       [".", "O", ".", ".", ".", "O", "."],
                       [".", ".", ".", ".", "O", ".", "."]]

        board4.grid = [["O", ".", "O", ".", "O", ".", "O"],
                       [".", "O", ".", ".", ".", "O", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", "."],
                       ["O", ".", "O", ".", "O", ".", "O"],
                       [".", "O", ".", ".", ".", "O", "."],
                       ["O", ".", ".", ".", ".", ".", "."]]

        # For each testing board above.
        for board in [board1, board2, board3, board4]:

            # This only works because the test boards are square.
            # If we omit this line, the Boards above are transposed
            # when compared to above. With this line, you can imagine
            # the list of lists above as the grid.
            board.grid = list(map(list, zip(*board.grid)))

            # Assert the helper method for detecting NE/SW diagonal runs
            # of the same symbol detects the winning NE/SW diagonal run.
            self.assertEqual(
                self.player.max_in_nesw_diagonal(board,
                                                 self.player.marker),
                board.win_condition,
                board.to_string()
            )

            # Assert the helper method for detecting NE/SW diagonal wins
            # detects the NE/SW diagonal win.
            self.assertTrue(
                self.player.win_nesw_diagonal(board, self.player.marker),
                board.to_string()
            )

            # Assert the overall win method detects a win
            self.assertTrue(
                self.player.have_i_won(board), board.to_string()
            )
