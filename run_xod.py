"""This file will run Naughts and Crosses and Dragons (XOD)."""

from src.Board import Board
from src.Human import Human
from src.CPU import CPU

def main():
    """Run the XOD game loop."""
    board = Board()

    player_1 = CPU('X', 'O')
    player_2 = CPU('O', 'X')

    board.display()
    while True:
        player_1.move(board)
        board.display()

        winner = board.is_there_a_winner()
        if winner == player_1.marker:
            print('Player %s has won!' % winner)
            break
        elif winner == '-':
            print('No winners.')
            break

        player_2.move(board)
        board.display()

        winner = board.is_there_a_winner()
        if winner == player_2.marker:
            print('Player %s has won!' % winner)
            break
        elif winner == '-':
            print('No winners.')
            break

if __name__ == '__main__':
    main()
