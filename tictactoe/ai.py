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
from datetime import now
import game

boards = 0


class Node:
    wins = 0.0
    games = 0.0
    move = ''
    board = []
    player_id = ''
    children = []

    def __init__(self, board, player_id):
        self.board = board
        self.player_id = player_id

    def get_children():
        return self.children


def mcts(node, time, start) -> (int, int):
    """
    # mcts

    This function implements a Monte-Carlo Tree Search.

    """
    best_score = -inf
    best_move = 0
    if now() >= start + time:
        if node.get_children():
            for child in node.get_children:
                if child.wins / child.games > best_score:
                    best_score = child.wins / child.games
                    best_move = child.move
            return (best_move, best_score)
        else:
            return None

    return (0,0)


def ai_move(board, player_id):
    """
    ai_move is a wrapper for the minimax_ab function.
    """

    global boards
    boards = 0

    root = Node(board, player_id)
    move, _ = mcts(root, 15, now())

    if move is None:
        move = randint(0, 24)

    board[move] = player_id
    print(f"Calls to minimax_ab: {boards}")
