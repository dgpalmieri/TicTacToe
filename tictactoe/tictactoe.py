"""
tictactoe.py
Dylan Palmieri
2021-02-07
main function for 5x5 Tic-Tac-Toe

This module contains the main UI loop for the tictactoe module.

It holds the read_file, replay_game, and main functions.
"""


from time import sleep
from game import game
from game import print_board


def read_file(board):
    """
    This function loads the last board state from a file,
    specified by an absolute path.
    """
    path = input("Please enter the absolute path of the game file: ")
    state = ""
    with open(path, "r") as fin:
        line = ""
        for line in fin:
            pass
        state = line

    for i in range(25):
        board[i] = state[i]

    return path


def replay_game():
    """
    This function reads a board state from a file, and calls the
    game.print_board function to print the board state.
    """
    path = input("Please enter the absolute path of the game file: ")
    board = []
    for _ in range(25):
        board.append(' ')
    with open(path, "r") as fin:
        for line in fin:
            for i in range(25):
                board[i] = line[i]
            print_board(board)
            sleep(1)


def main():
    """
    The main function holds the main UI for the tictactoe module.
    """
    while True:
        board = []
        path = ""
        for _ in range(25):
            board.append(' ')

        print("Welcome to 5x5 Tic-Tac-Toe!")
        print("At this juncture, you have several options:")
        print("[1] Play a new game.")
        print("[2] Continue a game (requires file input).")
        print("[3] Watch a previously played game (requires file input).")
        print("[4] Exit the game.")
        option = input("Choose an option 1/2/3/4: ")

        if option not in ('1', '2', '3', '4'):
            print("Please choose a valid option, either 1, 2, 3, or 4")
            continue

        if option == '2':  # start a saved game
            path = read_file(board)

        if option == '3':  # watch a previous game
            replay_game()
            print("End of File reached.")
            continue

        if option == '4':
            exit()

        print("Would you like to play against:")
        print("[1] A human player.")
        print("[2] An AI player.")
        print("[3] I'd like to watch two AI players play.")
        print("[4] Exit the game.")
        player = input("Please choose either 1, 2, 3, or 4: ")
        if player not in ('1', '2', '3'):
            if player == "4":
                break
            print("Please choose again.")
            continue

        game(board, path, player)

    print("Goodbye.")


if __name__ == '__main__':
    main()
