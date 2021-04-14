"""
ai.py
Dylan Palmieri
2021-02-08
AI functionality for 5x5 Tic-Tac-Toe

This module contains the AI functionality for the tictactoe game.
It holds the ai_move function, which is a wrapper for the mcts
workhorse function.
"""


from math import inf
from random import randint
import game

boards = 0


class Node:
    wins = 0
    games = 0
    children = []

    def get_children():
        return self.children


def mcts(board, player_id, depth, maximize, alpha=-inf, beta=-inf) -> (int, int):
    """
    # mcts

    This function implements a Monte-Carlo Tree Search.

    """


def ai_move(board, player_id):
    """
    ai_move is a wrapper for the minimax_ab function.
    """

    global boards
    boards = 0

    move, _ = mcts(board, player_id, 6, True)

    if move is None:
        move = randint(0, 24)

    board[move] = player_id
    print(f"Calls to minimax_ab: {boards}")
