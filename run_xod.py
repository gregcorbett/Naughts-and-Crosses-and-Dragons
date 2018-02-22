"""This file will run Naughts and Crosses and Dragons (XOD)."""

from src.Board import Board
from src.Human import Human
from src.CPU import CPU


def main():
    """Run the XOD game loop."""
    board = Board(11, 11, 5)

    player_1 = Human('X')
    player_2 = CPU('O', 'X')

    board.display()
    while True:

        if player_1.get_possible_moves(board) == []:
            print('No winners.')
            break

        player_1.move(board)
        board.display()

        if player_1.have_i_won(board):
            print('Player %s has won!' % player_1.marker)
            break

        if player_2.get_possible_moves(board) == []:
            print('No winners.')
            break

        player_2.move(board)
        board.display()

        if player_2.have_i_won(board):
            print('Player %s has won!' % player_2.marker)
            break


if __name__ == '__main__':
    main()
