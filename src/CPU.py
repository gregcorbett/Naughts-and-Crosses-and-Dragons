"""This file contains the CPU (player) class."""

import random

from src.Player import Player

class CPU(Player):
    """This class represents a CPU player."""

    def __init__(self, marker):
        """Create a new CPU player."""
        super().__init__(marker)

    def move(self, board):
        """Make a move."""
        moved = False
        while not moved:
            x_cord = random.randint(0, board.width - 1)
            y_cord = random.randint(0, board.height - 1)

            moved = self._place_marker((x_cord, y_cord), board)
