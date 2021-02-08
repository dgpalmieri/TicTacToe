# game.py
# Dylan Palmieri
# 2021-02-07
# Main game functions for 5x5 Tic-Tac-Toe

import ai
from time import localtime, strftime, sleep


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

    # Possible draw
    for char in board:
        if (char == ' '):
            continue
        return "draw"

    return ' '


def save_game(path, board_list):
    if (path == ""):
        path = "tictactoe_"
        path = path + strftime("%Y-%m-%d_%H:%M:%S", localtime())

    with open(path, "a") as fout:
        for elem in board_list:
            fout.write(''.join(elem))
            fout.write("\n")
    print("Your game has been saved as {}".format(path))


def game(board, path=""):
    while(True):
        print("Would you like to play against:")
        print("[1] A human player.")
        print("[2] An AI player.")
        print("[3] I'd like to watch two AI players play.")
        print("[4] Exit the game.")
        player = input("Please choose either 1, 2, 3, or 4: ")
        if (player != "1" and player != "2" and player != "3"):
            if (player == "4"):
                return -1
            print("Please choose again.")
            continue
        break

    board_list = []

    empty_board = []
    for _ in range(25):
        empty_board.append(" ")

    if (board != empty_board):
        turn = 0
        for char in board:
            if (char == 'X'):
                turn += 1
            elif (char == 'O'):
                turn -= 1

        if (turn == 0):
            turn = 'X'
        elif (turn == -1):
            turn = 'O'

        print("Based on the state of the board, I can see that", end="")
        print("it is {}'s turn.".format(turn))

        if (turn == 'O'):
            if (player == '2'):
                print("AI move:")
                ai.AI_move(board)
            else:
                while(True):
                    print("\'O\' player's move:")
                    print("Where would you like to place your \'O\'? ")
                    print("Format your move as a number between 1 ", end="")
                    print("and 25, with 1 being the top left square ", end="")
                    print("and 25 being the bottom right.")
                    move = input("Please enter your move: ")
                    move = int(move)

                    if (move > 0 and move < 26 and board[move] != 'X' and
                            board[move] != 'O'):
                        move = int(move)-1
                        board[move] = 'O'
                        break
                    else:
                        print("Please enter a valid move.")
                        continue

    turn = 'X'

    while(True):
        board_list.append(board.copy())
        print("This is the current board state:")
        print_board(board)
        print("It is \'{}\' player's move:".format(turn))
        if ((turn == 'O' and player == '2') or player == '3'):
            ai.AI_move(board, turn)
            sleep(1)
        else:
            save = input("Would you like to save the game and quit? y/n ")
            if (save.lower() == 'y'):
                save_game(path, board_list)
                return 2
            elif (save.lower() == 'n'):
                pass
            else:
                continue
            print("Where would you like to place your \'{}\'?".format(turn))
            print("Format your move as a number between 1 and 25, ", end="")
            print("with 1 being the top left square and 25 the bottom right.")
            move = input("Please enter your move: ")
            move = int(move)-1
            if (move >= 0 and move <= 24 and board[move] != 'X' and
                    board[move] != 'O'):
                board[move] = turn
            else:
                print("Please enter a valid move.")
                continue
        if (turn == 'X'):
            turn = 'O'
        else:
            turn = 'X'

        winner = check_win(board)
        if (winner == 'X' or winner == 'O'):
            print("We have a winner! \'{}\' wins!".format(winner))
            print_board(board)
        elif (winner == "draw"):
            print("It's a draw!")
        else:
            continue

        save = input("Would you like to save the game? y/n ")
        if (save.lower() == 'y'):
            save_game(path, board_list)
        return

