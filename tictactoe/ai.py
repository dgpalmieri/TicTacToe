"""
ai.py
Dylan Palmieri
2021-02-08
AI functionality for 5x5 Tic-Tac-Toe

This module contains the AI functionality for the tictactoe game.
It holds the ai_move function, which is a wrapper for the mcts
workhorse function.
"""


from math import inf, sqrt, log
from random import randint
import time
import game

boards = 0


class Node:
    wins = 0.0
    games = 0.0
    move = 0
    board = []
    player_id = ''
    children = []

    def __init__(self, board, player_id, move):
        self.board = board
        self.player_id = player_id
        self.move = move

    def get_children():
        return self.children


def mcts(node) -> (int, int):
    """
    # mcts
    This function implements a Monte-Carlo Tree Search.
    """
    node.games += 1

    if game.check_win(node.board):
        node.wins += 1
        return node.move

    # Selection
    next_move = -1
    next_player = 'O' if node.player_id == 'X' else 'X'
    next_board = copy(board)
    if node.get_children():
        max_uct = -inf
        for child in node.get_children():
            uct = child.wins/child.games + sqrt(log(node.games) / child.games)
            if uct > max_uct:
                max_uct = uct
                next_move = child.move

    # Expansion and Simulation
    else:
        move = random(0, 24)
        while node.board[move] != ' ':
            move = random(0, 24)

    next_board[move] = next_player
    next_node = Node(next_board, next_player, next_move)
    node.children.append(next_node)

    mcts(next_node)

    # Back-Propogation
    best_score = -inf
    best_move = -1
    if time() >= start + time:
        if node.get_children():
            for child in node.get_children():
                if child.wins / child.games > best_score:
                    best_score = child.wins / child.games
                    best_move = child.move
        return best_move

    return (0,0)


def ai_move(board, player_id):
    """
    # ai_move
    ai_move is a wrapper for the mcts function.
    """

    global boards
    boards = 0

    move = -1
    root = Node(board, player_id, -1)
    start = time.time()
    turn_length = 15
    while time.time() < start + turn_length:
        move = mcts(root)

    if move == -1:
        move = randint(0, 24)

    board[move] = player_id
    print(f"Calls to minimax_ab: {boards}")
