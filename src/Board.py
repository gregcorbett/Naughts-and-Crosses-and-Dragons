"""This file contains the board class."""

class Board:
    """This class represents the Game 'Board'."""

    def __init__(self, width=18, height=18, win_condition=3):
        """Create a new 'Board'."""
        self.height = height
        self.width = width
        self.win_condition = win_condition
        self.grid = [['.' for x in range(self.height)] for y in range(self.width)]

    def display(self):
        """Display the 'Board'."""
        for y_cord in range(self.height):
            for x_cord in range(self.width):
                print(self.grid[x_cord][y_cord], end='')
                if x_cord != self.width-1:
                    print(' ', end='')
            print()
        print()
