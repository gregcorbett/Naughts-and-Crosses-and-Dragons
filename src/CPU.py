"""This file contains the CPU (player) class."""

import copy

from src.Player import Player

class CPU(Player):
    """This class represents a CPU player."""

    def __init__(self, marker, opponent_marker):
        """Create a new CPU player."""
        super().__init__(marker)
        self.opponent_marker = opponent_marker
        self.search_depth_limit = 2

    def move(self, board):
        """Make a move."""
        print('Player %s is thinking!: ' % self.marker)

        (cord, _) = self.max_play(board, float('-inf'), float('inf'), 1)

        self._place_marker(cord, board)

    def evaluate_incomplete_board(self, board):
        """Return a heursitic value of the given Board."""
        heursitic = 0

        # Currently, the heuristic is quite simple and is the sum of the
        # longest line of this player's symbols (in each of the four
        # directions) minus the same for value for your opponent's marker.

        # Check horizontally
        heursitic = heursitic + self.max_in_row(board, self.marker)
        heursitic = heursitic - self.max_in_row(board, self.opponent_marker)

        # Check vertically
        heursitic = heursitic + self.max_in_column(board, self.marker)
        heursitic = heursitic - self.max_in_column(board, self.opponent_marker)

        # Check diagonally (SE)
        heursitic = heursitic + self.max_in_nwse_diagonal(board,
                                                          self.marker)
        heursitic = heursitic - self.max_in_nwse_diagonal(board,
                                                          self.opponent_marker)

        # Check diagonally (SW)
        heursitic = heursitic + self.max_in_nesw_diagonal(board,
                                                          self.marker)
        heursitic = heursitic - self.max_in_nesw_diagonal(board,
                                                          self.opponent_marker)

        return heursitic

    def max_play(self, board, alpha, beta, depth=1):
        """
        Return the 'best' move and it predicted value.

        Where the 'best' move maximises the minimum possible predicted value.
        """
        moves = self.get_possible_moves(board)

        if moves == []:
            # then it is a draw
            return (None, 0)

        best_move = moves[0]
        best_score = float('-inf')

        for move in moves:
            clone_state = copy.deepcopy(board)
            self._place_marker(move, clone_state, self.marker)

            if self.has_marker_won(clone_state, self.marker):
                # Then I have won! Huzzah!
                # But factor in how far down
                # the tree the win is.
                score = 1000000 / depth
            elif depth > self.search_depth_limit:
                # Rather than do minimax to determine the best move,
                # just use a heuristic.
                score = self.evaluate_incomplete_board(clone_state)
            else:
                # Use minimax recursively to determine the best move.
                (_, score) = self.min_play(clone_state, alpha, beta, depth + 1)

            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
            if score > best_score:
                best_score = score
                best_move = move

        return (best_move, best_score)

    def min_play(self, board, alpha, beta, depth=1):
        """
        Return the 'best' move and it predicted value.

        Where the 'best' move minimises the maximum possible predicted value.
        """
        moves = self.get_possible_moves(board)

        if moves == []:
            # then it is a draw
            return (None, 0)

        best_move = moves[0]
        best_score = float('inf')

        for move in moves:
            clone_state = copy.deepcopy(board)
            self._place_marker(move, clone_state, self.opponent_marker)

            if self.has_marker_won(clone_state, self.opponent_marker):
                # Then I have lost! Booooooo!
                # But factor in how far down
                # the tree the loss is.
                score = -1000000 / depth
            elif depth > self.search_depth_limit:
                # Rather than do minimax to determine the best move,
                # just use a heuristic.
                score = - self.evaluate_incomplete_board(clone_state)
            else:
                # Use minimax recursively to determine the best move.
                (_, score) = self.max_play(clone_state, alpha, beta, depth + 1)

            beta = min(beta, best_score)

            if beta <= alpha:
                break
            if score < best_score:
                best_score = score
                best_move = move

        return (best_move, best_score)
