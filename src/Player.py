"""This file contains the Player class."""

class Player():
    """A Base class to be extended to create specifc player types."""
    def __init__(self, marker):
        """Create new Player object."""
        self.marker = marker

    def _place_marker(self, co_ord, board):
        """Place a marker on the board."""
        if board.grid[co_ord[0]][co_ord[1]] == '.':
            board.grid[co_ord[0]][co_ord[1]] = self.marker
            return True
        return False

    def has_won(self, board):
        """Check if the Player has won the given Board."""
        # Check horizontally
        for y_cord in range(board.height - board.win_condition):
            for x_cord in range(board.width - board.win_condition):
                line_start = board.grid[x_cord][y_cord]
                if line_start is not self.marker:
                    continue
                for n_cord in range(1, board.win_condition):
                    if board.grid[x_cord+n_cord][y_cord] != self.marker:
                        break
                    elif n_cord == (board.win_condition - 1):
                        return True

        # Check vertically
        for y_cord in range(board.height - board.win_condition):
            for x_cord in range(board.width - board.win_condition):
                line_start = board.grid[x_cord][y_cord]
                if line_start is not self.marker:
                    continue
                for n_cord in range(1, board.win_condition):
                    if board.grid[x_cord][y_cord+n_cord] != self.marker:
                        break
                    elif n_cord == (board.win_condition - 1):
                        return True

        # Check diagonally (one way)
        for y_cord in range(board.height - board.win_condition):
            for x_cord in range(board.width - board.win_condition):
                line_start = board.grid[x_cord][y_cord]
                if line_start is not self.marker:
                    continue
                for n_cord in range(1, board.win_condition):
                    if board.grid[x_cord+n_cord][y_cord+n_cord] != self.marker:
                        break
                    elif n_cord == (board.win_condition - 1):
                        return True

        # Check diagonally (one way)
        for y_cord in range(board.height - board.win_condition):
            for x_cord in range(board.width - board.win_condition):
                line_start = board.grid[x_cord][y_cord]
                if line_start is not self.marker:
                    continue
                for n_cord in range(1, board.win_condition):
                    if board.grid[x_cord-n_cord][y_cord-n_cord] != self.marker:
                        break
                    elif n_cord == (board.win_condition - 1):
                        return True

        # Check diagonally (one way)
        for y_cord in range(board.height - board.win_condition):
            for x_cord in range(board.width - board.win_condition):
                line_start = board.grid[x_cord][y_cord]
                if line_start is not self.marker:
                    continue
                for n_cord in range(1, board.win_condition):
                    if board.grid[x_cord+n_cord][y_cord-n_cord] != self.marker:
                        break
                    elif n_cord == (board.win_condition - 1):
                        return True

        # Check diagonally (one way)
        for y_cord in range(board.height - board.win_condition):
            for x_cord in range(board.width - board.win_condition):
                line_start = board.grid[x_cord][y_cord]
                if line_start is not self.marker:
                    continue
                for n_cord in range(1, board.win_condition):
                    if board.grid[x_cord-n_cord][y_cord+n_cord] != self.marker:
                        break
                    elif n_cord == (board.win_condition - 1):
                        return True
        # You have not won
        return False

    def move(self, board):
        """Not Implemented. Override in Sub Class."""
        raise NotImplementedError
