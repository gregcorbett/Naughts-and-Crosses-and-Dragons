"""This file contains the Dragon (player) class."""

import time
import random

from src.Player import Player

class Dragon(Player):
    """This class represents a Dragon player."""

    def __init__(self):
        """Create a new Dragon player."""
        super().__init__(' ')

    def move(self, board):
        """Make a move."""
        print('The Dragon flies over head... ', end='')
        
        dragon_anger = random.randint(1,20)
        
        time.sleep(dragon_anger / 4)
        if dragon_anger == 19:
            print('and launches a small fireball.')
            x_cord = random.randint(1, board.width - 2)
            y_cord = random.randint(1, board.height - 2)
            board.grid[x_cord][y_cord] = ' '
                
        elif dragon_anger == 20:
            print('and launches a large fireball.')
            x_cord = random.randint(1, board.width - 2)
            y_cord = random.randint(1, board.height - 2)
            for i_cord in range(-1,2):
                for j_cord in range(-1,2):
                    board.grid[x_cord+i_cord][y_cord+j_cord] = ' '
            
        else:
            print('But nothing happpens.')
        
        print()


