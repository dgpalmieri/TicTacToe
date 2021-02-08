# tictactoe.py
# Dylan Palmieri
# 2021-02-07
# main function for 5x5 Tic-Tac-Toe

import ai
import game as g
from time import sleep


def read_file(board):
    path = input("Please enter the absolute path of the game file: ")
    state = ""
    with open(path, "r") as fin:
        for line in fin:
            pass
        state = line

    for i in range(25):
        board[i] = state[i]

    return path


def replay_game():
    path = input("Please enter the absolute path of the game file: ")
    board = []
    for _ in range(25):
        board.append(' ')
    with open(path, "r") as fin:
        for line in fin:
            for i in range(25):
                board[i] = line[i]
            g.print_board(board)
            sleep(1)
    return


def main():
    game = input("Hello. Would you like to play a game? y/n: ")
    if (game.lower() == 'y'):
        while(True):

            print("At this juncture, you have several options:")
            print("[1] Play a new game.")
            print("[2] Continue a game (requires file input).")
            print("[3] Watch a previously played game (requires file input).")
            print("[4] Exit the game.")
            option = input("Choose an option 1/2/3/4: ")

            board = []
            for _ in range(25):
                board.append(" ")

            if (option == '1'):  # play a new game
                exit = g.game(board)
                if (exit == -1):
                    break
                if (exit == 1):
                    continue

            elif (option == '2'):  # start a saved game
                path = read_file(board)
                exit = g.game(board, path)
                if (exit == -1):
                    break
                if (exit == 1):
                    continue

            elif(option == '3'):  # watch a previous game
                replay_game()
                print("End of File reached.")
                continue

            elif (option == '4'):
                break

            else:
                option = input("Please choose a valid option,\
                               either 1, 2, 3, or 4:")

        print("Goodbye.")


if __name__ == '__main__':
    main()
