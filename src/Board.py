"""This file contains the board class."""

class Board:
    """This class represents the Game 'Board'."""

    def __init__(self, height=18, width=18, win_condition=3):
        """Create a new 'Board'."""
        self.height = height
        self.width = width
        self.win_condition = win_condition
        self.grid = [['.' for x in range(self.width)] for y in range(self.height)]

    def display(self):
        """Display the 'Board'."""
        for y_cord in range(self.height):
            for x_cord in range(self.width):
                print(self.grid[x_cord][y_cord], end='')
                if x_cord != self.width-1:
                    print(' ', end='')
            print()
        print()
