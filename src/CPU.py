"""This file contains the CPU (player) class."""

import copy

from src.Player import Player

class CPU(Player):
    """This class represents a CPU player."""

    def __init__(self, marker, opponent_marker):
        """Create a new CPU player."""
        super().__init__(marker)
        self.opponent_marker = opponent_marker

    def move(self, board):
        """Make a move."""
        print('Player %s is thinking!: ' % self.marker)

        (cord, _) = self.max_play(board, float('-inf'), float('inf'), 1)

        self._place_marker(cord, board)

    def evaluate_incomplete_board(self, board, marker):
        """Return a heursitic value of the given Board."""
        heursitic = 0
        return_n = 0
        moves_made = 0

        # Count the moves made to normalize heursitic
        for y_cord in range(board.height):
            for x_cord in range(board.width):
                if board.grid[x_cord][y_cord] != '.':
                    moves_made = moves_made + 1

        # Check horizontally
        for y_cord in range(board.height):
            for x_cord in range(board.width - board.win_condition + 1):
                line_start = board.grid[x_cord][y_cord]
                if line_start != marker:
                    continue
                for n_cord in range(1, board.win_condition):
                    if board.grid[x_cord+n_cord][y_cord] != line_start:
                        break
                    return_n = n_cord

                heursitic = heursitic + return_n + 1

        # Check vertically
        for y_cord in range(board.height - board.win_condition + 1):
            for x_cord in range(board.width):
                line_start = board.grid[x_cord][y_cord]
                if line_start != marker:
                    continue
                for n_cord in range(1, board.win_condition):
                    if board.grid[x_cord][y_cord+n_cord] != line_start:
                        break
                    return_n = n_cord

                heursitic = heursitic + return_n + 1

        # Check diagonally (SE) # correct!
        for y_cord in range(board.height - board.win_condition +1):
            for x_cord in range(board.width - board.win_condition +1):
                line_start = board.grid[x_cord][y_cord]
                if line_start != marker:
                    continue
                for n_cord in range(1, board.win_condition):
                    if board.grid[x_cord+n_cord][y_cord+n_cord] != line_start:
                        break
                    return_n = n_cord

                heursitic = heursitic + return_n + 1

        # Check diagonally (SW)
        for y_cord in range(board.height - board.win_condition + 1):
            for x_cord in range(board.win_condition - 1, board.width):
                line_start = board.grid[x_cord][y_cord]
                if line_start != marker:
                    continue
                for n_cord in range(1, board.win_condition):
                    if board.grid[x_cord-n_cord][y_cord+n_cord] != line_start:
                        break
                    return_n = n_cord

                heursitic = heursitic + return_n + 1

        # return heursitic divided by 4 as we count each space 4 times
        return heursitic / (4 * moves_made)

    def max_play(self, board, alpha, beta, depth):
        """
        Return the 'best' move and it predicted value.

        Where the 'best' move maximises the minimum possible predicted value.
        """
        if board.is_there_a_winner() == self.opponent_marker:
            # then I have lost
            return (None, float('-inf'))
        elif board.get_possible_moves() == []:
            # then it is a draw
            return (None, 0)
        elif depth < 0:
            # Rather than do minimax to determine the best move
            # use a heuristic
            return (None, self.evaluate_incomplete_board(board, self.marker))

        moves = board.get_possible_moves()
        best_move = moves[0]
        best_score = float('-inf')

        for move in moves:
            clone_state = copy.deepcopy(board)
            self._place_marker(move, clone_state, self.marker)
            (_, score) = self.min_play(clone_state, alpha, beta, depth - 1)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
            if score > best_score:
                best_score = score
                best_move = move

        return (best_move, best_score)

    def min_play(self, board, alpha, beta, depth):
        """
        Return the 'best' move and it predicted value.

        Where the 'best' move minimises the maximum possible predicted value.
        """
        if board.is_there_a_winner() == self.marker:
            # then I have won
            return (None, float('inf'))
        elif board.get_possible_moves() == []:
            return (None, 0)
        elif depth < 0:
            # Rather than do minimax to determine the best move
            # use a heuristic
            return (None, - self.evaluate_incomplete_board(board, self.opponent_marker))

        moves = board.get_possible_moves()
        best_move = moves[0]
        best_score = float('inf')

        for move in moves:
            clone_state = copy.deepcopy(board)
            self._place_marker(move, clone_state, self.opponent_marker)
            (_, score) = self.max_play(clone_state, alpha, beta, depth - 1)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
            if score < best_score:
                best_score = score
                best_move = move

        return (best_move, best_score)
