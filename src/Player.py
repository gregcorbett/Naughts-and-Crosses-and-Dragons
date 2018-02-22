"""This file contains the Player class."""


class Player():
    """A Base class to be extended to create specifc player types."""
    def __init__(self, marker):
        """Create new Player object."""
        self.marker = marker

    def _place_marker(self, co_ord, board, marker=None):
        """Place a marker on the board."""
        if marker is None:
            marker = self.marker
        if board.grid[co_ord[0]][co_ord[1]] == '.':
            board.grid[co_ord[0]][co_ord[1]] = marker
            return True
        return False

    def get_possible_moves(self, board):
        """Return a list of co-ordinates that are free."""
        possible_moves = []
        for y_cord in range(board.height):
            for x_cord in range(board.width):
                if board.grid[x_cord][y_cord] == '.':
                    possible_moves.append((x_cord, y_cord))

        return possible_moves

    def max_in_row(self, board, marker):
        """Return the max number of marker in a row."""
        count = 0
        for y_cord in range(board.height):
            for x_cord in range(board.width - board.win_condition + 1):
                line_start = board.grid[x_cord][y_cord]
                if line_start != marker:
                    continue
                for n_cord in range(1, board.win_condition):
                    if board.grid[x_cord+n_cord][y_cord] == line_start:
                        count = max(count, n_cord)
                    else:
                        break

        return count + 1

    def max_in_column(self, board, marker):
        """Return the max number of marker in a column."""
        count = 0
        for y_cord in range(board.height - board.win_condition + 1):
            for x_cord in range(board.width):
                line_start = board.grid[x_cord][y_cord]
                if line_start != marker:
                    continue
                for n_cord in range(1, board.win_condition):
                    if board.grid[x_cord][y_cord+n_cord] == line_start:
                        count = max(count, n_cord)
                    else:
                        break

        return count + 1

    def max_in_nwse_diagonal(self, board, marker):
        """Return the max number of marker in a NW/SE diagonal."""
        count = 0
        for y_cord in range(board.height - board.win_condition + 1):
            for x_cord in range(board.width - board.win_condition + 1):
                line_start = board.grid[x_cord][y_cord]
                if line_start != marker:
                    continue
                for n_cord in range(1, board.win_condition):
                    if board.grid[x_cord+n_cord][y_cord+n_cord] == line_start:
                        count = max(count, n_cord)
                    else:
                        break

        return count + 1

    def max_in_nesw_diagonal(self, board, marker):
        """Return the max number of marker in a NE/SW diagonal."""
        count = 0
        for y_cord in range(board.height - board.win_condition + 1):
            for x_cord in range(board.win_condition - 1, board.width):
                line_start = board.grid[x_cord][y_cord]
                if line_start != marker:
                    continue
                for n_cord in range(1, board.win_condition):
                    if board.grid[x_cord-n_cord][y_cord+n_cord] == line_start:
                        count = max(count, n_cord)
                    else:
                        break

        return count + 1

    def win_horizontal(self, board, marker):
        """True iff there is a winning row of marker on board."""
        return self.max_in_row(board, marker) == board.win_condition

    def win_vertical(self, board, marker):
        """True iff there is a winning column of marker on board."""
        return self.max_in_column(board, marker) == board.win_condition

    def win_nwse_diagonal(self, board, marker):
        """True iff there is a winning NW/SE diagonal of marker on board."""
        return self.max_in_nwse_diagonal(board, marker) == board.win_condition

    def win_nesw_diagonal(self, board, marker):
        """True iff there is a winning NE/SW diagonal of marker on board."""
        return self.max_in_nesw_diagonal(board, marker) == board.win_condition

    def has_marker_won(self, board, marker):
        """True iff the marker has won board."""
        return (self.win_horizontal(board, marker) or
                self.win_vertical(board, marker) or
                self.win_nwse_diagonal(board, marker) or
                self.win_nesw_diagonal(board, marker))

    def have_i_won(self, board):
        """True iff this player has won board."""
        return self.has_marker_won(board, self.marker)

    def move(self, board):
        """Not Implemented. Override in Sub Class."""
        raise NotImplementedError
