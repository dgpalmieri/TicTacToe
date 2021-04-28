"""
ai.py
Dylan Palmieri
2021-02-08
AI functionality for 5x5 Tic-Tac-Toe

This module contains the AI functionality for the tictactoe game.
It holds the ai_move function, which is a wrapper for either the
minimax or mcts workhorse function.
"""


from math import inf, sqrt, log
from random import randint
from copy import deepcopy
import time
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


class Node:
    def __init__(self, board, player_id, move):
        self.wins = 0.0
        self.games = 0.0
        self.move = move
        self.board = board
        self.player_id = player_id
        self.children = []


def mcts(node, expanding=False):
    """
    # mcts
    This function implements a Monte-Carlo Tree Search.
    """
    global boards
    boards += 1

    node.games += 1
    if game.check_win(node.board) != ' ':
        if game.check_win(node.board) == 'X' or game.check_win(node.board) == 'O':
            node.wins += 1
        return

    # Selection
    move = -1
    next_player = 'O' if node.player_id == 'X' else 'X'
    next_board = deepcopy(node.board)
    if len(node.children) == 25:
        max_uct = -inf
        for child in node.children:
            uct = child.wins/child.games + sqrt(log(node.games) / child.games)
            if uct > max_uct:
                max_uct = uct
                move = child.move

    # Expansion and Simulation
    elif not expanding:
        for move_expansion in range(25):
            if node.board[move_expansion] != ' ':
                continue
            next_board = deepcopy(node.board)
            next_board[move_expansion] = node.player_id
            next_node = Node(next_board, next_player, move_expansion)
            is_child = False
            for child in node.children:
                if child.board == next_board:
                    next_node = child
                    is_child = True
            if not is_child:
                node.children.append(next_node)
            mcts(next_node, True)
    else:
        move = randint(0, 24)
        while node.board[move] != ' ':
            move = randint(0, 24)
        next_board[move] = node.player_id
        next_node = Node(next_board, next_player, move)
        is_child = False
        for child in node.children:
            if child.board == next_board:
                next_node = child
                is_child = True
        if not is_child:
            node.children.append(next_node)
        mcts(next_node, expanding)

    # Back-Propagation
    node.wins = 0
    node.games = 0
    if node.children:
        for child in node.children:
            node.wins += child.games - child.wins
            node.games += child.games


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

    """
    # ai_move
    ai_move is a wrapper for the mcts function.

    global boards

    move = -1
    root = Node(board, player_id, -1)
    start = time.time()
    turn_length = 15
    while time.time() < start + turn_length:
        mcts(root)

    best_score = -inf
    print(f"length of children: {len(root.children)}")
    for child in root.children:
        if child.wins / child.games > best_score:
            move = child.move
            best_score = child.wins / child.games

    if move == -1:
        print("Random move")
        move = randint(0, 24)

    board[move] = player_id
    print(f"Calls to mcts: {boards}")
    """

