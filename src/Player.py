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

    def move(self, board):
        """Not Implemented. Override in Sub Class."""
        raise NotImplementedError
