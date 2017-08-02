"""This file contains the CPU (player) class."""

import copy

from src.Player import Player

class CPU(Player):
    """This class represents a CPU player."""

    def __init__(self, marker):
        """Create a new CPU player."""
        super().__init__(marker)

    def move(self, board):
        """Make a move."""
        print('Player %s is thinking!: ' % self.marker)

        (x_cord, y_cord) = self.minimax(board)

        self._place_marker((x_cord, y_cord), board)

    def minimax(self, board):
        """Use the minimax algorthim to determine the best move to make."""
        moves = board.get_possible_moves()
        best_move = moves[0]
        best_score = float('-inf')
        for move in moves:
            clone_state = copy.deepcopy(board)
            self._place_marker(move, clone_state, 'O')
            score = self.min_play(clone_state)
            if score > best_score:
                best_move = move
                best_score = score

        return best_move

    def max_play(self, board):
        """Helper method for minimax."""
        if board.is_there_a_winner() == 'X':
            # then X has won
            return -100
        elif board.get_possible_moves() == []:
            # then it is a draw
            return 0

        best_score = float('-inf')
        for move in board.get_possible_moves():
            clone_state = copy.deepcopy(board)
            self._place_marker(move, clone_state, 'O')
            score = self.min_play(clone_state)
            if score > best_score:
                best_score = score

        return best_score

    def min_play(self, board):
        """Helper method for minimax."""
        if board.is_there_a_winner() == 'O':
            # then O has won
            return 100
        elif board.get_possible_moves() == []:
            return 0

        best_score = float('inf')
        for move in board.get_possible_moves():
            clone_state = copy.deepcopy(board)
            self._place_marker(move, clone_state, 'X')
            score = self.max_play(clone_state)
            if score < best_score:
                best_score = score

        return best_score
