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

    def get_possible_moves(self):
        """Return a list of co-ordinates that are free."""
        possible_moves = []
        for y_cord in range(self.height):
            for x_cord in range(self.width):
                if self.grid[x_cord][y_cord] == '.':
                    possible_moves.append((x_cord, y_cord))

        return possible_moves

    def is_there_a_winner(self):
        """Check if this Player has won the given self.grid."""
        # Check horizontally
        for y_cord in range(self.height):
            for x_cord in range(self.width - self.win_condition + 1):
                line_start = self.grid[x_cord][y_cord]
                if line_start == '.':
                    continue
                for n_cord in range(1, self.win_condition):
                    if self.grid[x_cord+n_cord][y_cord] != line_start:
                        break
                    elif n_cord == (self.win_condition - 1):
                        return line_start

        # Check vertically
        for y_cord in range(self.height - self.win_condition + 1):
            for x_cord in range(self.width):
                line_start = self.grid[x_cord][y_cord]
                if line_start == '.':
                    continue
                for n_cord in range(1, self.win_condition):
                    if self.grid[x_cord][y_cord+n_cord] != line_start:
                        break
                    elif n_cord == (self.win_condition - 1):
                        return line_start

   # Check diagonally (SE) # correct!
        for y_cord in range(self.height - self.win_condition +1):
            for x_cord in range(self.width - self.win_condition +1):
                line_start = self.grid[x_cord][y_cord]
                if line_start == '.':
                    continue
                for n_cord in range(1, self.win_condition):
                    if self.grid[x_cord+n_cord][y_cord+n_cord] != line_start:
                        break
                    elif n_cord == (self.win_condition - 1):
                        return line_start

        # Check diagonally (SW)
        for y_cord in range(self.height - self.win_condition + 1):
            for x_cord in range(self.width):
                line_start = self.grid[x_cord][y_cord]
                if line_start == '.':
                    continue
                for n_cord in range(1, self.win_condition):
                    if x_cord-n_cord < 0:
                        # then don't check as you will be wrapping
                        # arround the board
                        break
                    elif self.grid[x_cord-n_cord][y_cord+n_cord] != line_start:
                        break
                    elif n_cord == (self.win_condition - 1):
                        return line_start

        # There are no winners!
        # Check if the game is over
        if self.get_possible_moves() == []:
            return '-'

        # No winners but the game is not over!
        return None
