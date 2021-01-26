"""
ai.py
Dylan Palmieri
2021-02-08
AI functionality for 5x5 Tic-Tac-Toe

This module contains the AI functionality for the tictactoe game.
It holds the ai_move function, which is a wrapper for the minimax_ab
workhorse function.
"""


from math import inf
from random import randint
import game

boards = 0

def minimax_ab(board, player_id, depth, maximize, alpha=-inf, beta=-inf) -> (int, int):
    """
    # Minimax_ab

    This function implements a minimax game tree search with alpha/beta
    pruning.

    It returns a tuple of (int, int), which represents the most optimal
    move and that move's score, which is a sum of the different weights
    of the boards.

    The board weights are determined by the fastest possible win states.
    """
    winner = game.check_win(board)
    if winner == player_id:
        return None, 10 + depth
    if winner not in (' ', "draw"):
        return None, -10 - depth
    if winner == "draw":
        return None, 0
    if depth == 0:
        return None, None

    global boards
    boards += 1

    best_move = None
    value = None

    for i in range(25):
        if board[i] == ' ':
            board[i] = player_id
            _, value = minimax_ab(board,
                                  'O' if player_id == 'X' else 'X',
                                  depth - 1,
                                  False,
                                  alpha,
                                  beta)
            board[i] = ' '
            if (value is not None
               and (value > alpha if maximize else value < beta)):
                if maximize:
                    alpha = value
                else:
                    beta = value
                if (alpha != -inf and beta != inf
                   and alpha >= beta if maximize else beta >= alpha):
                    break
                best_move = i

    if maximize:
        return best_move, alpha

    return best_move, beta


def ai_move(board, player_id):
    """
    ai_move is a wrapper for the minimax_ab function.
    """

    global boards
    boards = 0

    move, _ = minimax_ab(board, player_id, 6, True)

    if move is None:
        move = randint(0, 24)

    board[move] = player_id
    print(f"Calls to minimax_ab: {boards}")
