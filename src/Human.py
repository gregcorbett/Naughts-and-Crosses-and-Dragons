"""This class contains the Human (player) class."""

from ast import literal_eval as make_tuple

from src.Player import Player

class Human(Player):
    """This class represents a Human player."""

    def __init__(self, marker):
        """Create a new Human player."""
        super().__init__(marker)

    def move(self, board):
        """Make a move."""
        moved = False
        while not moved:
            co_ord_input = input('Player %s, your move!: ' % self.marker)

            co_ord = make_tuple(co_ord_input)

            moved = self._place_marker(co_ord, board)
            
        return co_ord
