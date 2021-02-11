# ai.py
# Dylan Palmieri
# 2021-02-08
# AI functionality for 5x5 Tic-Tac-Toe

from random import randint
from game import check_win
from math import inf


def minimax(board, player_id, depth, maximize):
    winner = check_win(board)
    if winner == player_id:
        return None, 10 + depth
    elif winner != player_id and winner != ' ' and winner != "draw":
        return None, -10 - depth
    elif winner == "draw":
        return None, 0
    elif depth == 0:
        return None, None
    else:
        score = None
        if maximize:
            score = -inf
        else:
            score = inf

        best_move = None

        for i in range(25):
            if board[i] == ' ':
                board[i] = player_id
                _, value = minimax(board,
                                  'O' if player_id == 'X' else 'X',
                                  depth - 1,
                                  False)
                board[i] = ' '
                if (value is not None and
                    (value > score if maximize else value < score)):
                    score = value
                    best_move = i

        return best_move, score


def AI_move(board, player_id):

    move, _ = minimax(board, player_id, 5, True)
    print("move: ", move)

    if move == None:
        move = randint(0,24)
        print("random move")

    board[move] = player_id

    return
