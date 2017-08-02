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

        (cord, _) = self.max_play(board)

        self._place_marker(cord, board)

    def max_play(self, board):
        """
        Return the 'best' move and it predicted value.

        Where the 'best' move maximises the minimum possible predicted value.
        """
        if board.is_there_a_winner() == 'X':
            # then X has won
            return (None, -100)
        elif board.get_possible_moves() == []:
            # then it is a draw
            return (None, 0)

        moves = board.get_possible_moves()
        best_move = moves[0]
        best_score = float('-inf')

        for move in moves:
            clone_state = copy.deepcopy(board)
            self._place_marker(move, clone_state, 'O')
            (_, score) = self.min_play(clone_state)
            if score > best_score:
                best_score = score
                best_move = move

        return (best_move, best_score)

    def min_play(self, board):
        """
        Return the 'best' move and it predicted value.

        Where the 'best' move minimises the maximum possible predicted value.
        """
        if board.is_there_a_winner() == 'O':
            # then O has won
            return (None, 100)
        elif board.get_possible_moves() == []:
            return (None, 0)

        moves = board.get_possible_moves()
        best_move = moves[0]
        best_score = float('inf')

        for move in moves:
            clone_state = copy.deepcopy(board)
            self._place_marker(move, clone_state, 'X')
            (_, score) = self.max_play(clone_state)
            if score < best_score:
                best_score = score
                best_move = move

        return (best_move, best_score)
