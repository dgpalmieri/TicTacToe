# tictactoe.py
# Dylan Palmieri
# 2021-02-07
# main function for 5x5 Tic-Tac-Toe

import ai
import game as g


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

            if (option == '1'):
                board = []
                for _ in range(25):
                    board.append(" ")
                exit = g.game(board)
                if (exit == -1):
                    break
                if (exit == 1):
                    continue
            elif (option == '2'):
                pass
            elif(option == '3'):
                pass
            elif (option == '4'):
                break
            else:
                option = input("Please choose a valid option,\
                               either 1, 2, 3, or 4:")

        print("Goodbye.")


if __name__ == '__main__':
    main()
