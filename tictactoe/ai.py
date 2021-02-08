# ai.py
# Dylan Palmieri
# 2021-02-08
# AI functionality for 5x5 Tic-Tac-Toe

from random import randint


def AI_move(board, turn):
    num = randint(0, 24)

    while(board[num] != ' '):
        num = randint(0, 24)

    board[num] = turn

    return
