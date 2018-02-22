"""This file contains the Board class."""


class Board:
    """This class represents the Game 'Board'."""

    def __init__(self, width, height, win_condition):
        """Create a new 'Board'."""
        self.height = height
        self.width = width
        self.win_condition = win_condition
        self.grid = [['.'
                      for x in range(self.height)]
                     for y in range(self.width)]

    def display(self):
        """Display the Board."""
        print(self.to_string())
        print()

    def to_string(self):
        """Convert the Board to a string."""
        output = '\n'
        for y_cord in range(self.height):
            for x_cord in range(self.width):
                output = output + self.grid[x_cord][y_cord]
                if x_cord != self.width-1:
                    output = output + " "
            output = output + "\n"
        return output

    def __deepcopy__(self, memodict=None):
        """Override default deepcopy behaviour for Board objects."""
        copy_board = Board(self.width, self.height, self.win_condition)
        for x_cord in range(self.width):
            for y_cord in range(self.height):
                copy_board.grid[x_cord][y_cord] = self.grid[x_cord][y_cord]
        return copy_board
