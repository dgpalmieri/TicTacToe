# game.py
# Dylan Palmieri
# 2021-02-07
# Main game functions for 5x5 Tic-Tac-Toe

def print_board(board):
    if (len(board) < 25):
        print("Something's wrong with the board. len() < 25")
        return

    print()
    print()
    print("            |      |      |      |      ")
    print("        {}   |  {}   |  {}   |  {}   |  {}   ".format(
        board[0], board[1], board[2], board[3], board[4]))
    print("      ______|______|______|______|______")
    print("            |      |      |      |      ")
    print("        {}   |  {}   |  {}   |  {}   |  {}   ".format(
        board[5], board[6], board[7], board[8], board[9]))
    print("      ______|______|______|______|______")
    print("            |      |      |      |      ")
    print("        {}   |  {}   |  {}   |  {}   |  {}   ".format(
        board[10], board[11], board[12], board[13], board[14]))
    print("      ______|______|______|______|______")
    print("            |      |      |      |      ")
    print("        {}   |  {}   |  {}   |  {}   |  {}   ".format(
        board[15], board[16], board[17], board[18], board[19]))
    print("      ______|______|______|______|______")
    print("            |      |      |      |      ")
    print("        {}   |  {}   |  {}   |  {}   |  {}   ".format(
        board[20], board[21], board[22], board[23], board[24]))
    print("            |      |      |      |      ")
    print()
    print()


def check_win(board):
    # Possible Horizontal Wins
    horizontal = [0, 1, 5, 6, 10, 11, 15, 16, 20, 21]
    for i in horizontal:
        if (board[i] != ' ' and
                board[i] == board[i+1] == board[i+2] == board[i+3]):
            return board[i]

    # Possible Diagonal wins, left to right
    l_diagonal = [0, 1, 5, 6]
    for i in l_diagonal:
        if (board[i] != ' ' and
                board[i] == board[i+5+1] == board[i+10+2] == board[i+15+3]):
            return board[i]

    # Possible Diagonal wins, right to left
    r_diagonal = [3, 4, 8, 9]
    for i in r_diagonal:
        if (board[i] != ' ' and
                board[i] == board[i+5-1] == board[i+10-2] == board[i+15-3]):
            return board[i]

    # Possible Vertical wins
    for i in range(10):
        if (board[i] != ' ' and
                board[i] == board[i+5] == board[i+10] == board[i+15]):
            return board[i]

    return ' '
