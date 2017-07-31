"""This file will run Naughts and Crosses and Dragons (XOD)."""

from src.Board import Board
from src.Human import Human
from src.CPU import CPU

def main():
    """Run the XOD game loop."""
    board = Board()

    player_1 = Human('X')
    player_2 = CPU('O')

    board.display()
    while True:
        player_1.move(board)
        board.display()
        if player_1.has_won(board):
            print('Player %s has won!' % player_1.marker)
            break

        player_2.move(board)
        board.display()
        if player_2.has_won(board):
            print('Player %s has won!' % player_2.marker)
            break

if __name__ == '__main__':
    main()
