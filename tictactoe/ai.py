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
from copy import copy
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

    def get_children(self):
        return self.children


def mcts(node):
    """
    # mcts
    This function implements a Monte-Carlo Tree Search.
    """
    node.games += 1

    if game.check_win(node.board) != ' ':
        node.wins += 1
        return

    # Selection
    move = -1
    next_player = 'O' if node.player_id == 'X' else 'X'
    next_board = copy(node.board)
    if node.get_children():
        max_uct = -inf
        for child in node.get_children():
            uct = child.wins/child.games + sqrt(log(node.games) / child.games)
            if uct > max_uct:
                max_uct = uct
                move = child.move

    # Expansion and Simulation
    else:
        move = randint(0, 24)
        while node.board[move] != ' ':
            move = randint(0, 24)

    next_board[move] = node.player_id
    next_node = Node(next_board, next_player, move)
    node.children.append(next_node)  # appends next_node to node.children and next_node.children

    mcts(next_node)

    # Back-Propagation
    if node.get_children():
        for child in node.get_children():
            node.games += child.games
            node.wins += child.games - child.wins


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
        mcts(root)

    best_score = inf
    print(f"length of children: {len(root.children)}")
    for child in root.children:
        if child.wins / child.games < best_score:
            move = child.move
            best_score = child.wins / child.games

    if move == -1:
        print("Random move")
        move = randint(0, 24)

    board[move] = player_id
    print(f"Calls to minimax_ab: {boards}")
