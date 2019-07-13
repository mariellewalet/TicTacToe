""" JUST ADDING BASIC FILE TO GITHUB

GOAL PROJECT :
  - CREATE A TIC TAC TOE THAT WORKS AND LOOKS GOOD
  - NO COPYING FULL CODE FROM INTERNET
  - LEARN PYGAMES
  - COMMENT WELL
  - WRITE THE PYTHONIC WAY AND NOT JAVA !!!!!"""

import random

# board is a 2D array with [row][column]
board = {
    0: {
        0: -1,
        1: -1,
        2: -1,
    },
    1: {
        0: -1,
        1: -1,
        2: -1,
    },
    2: {
        0: -1,
        1: -1,
        2: -1,
    },
}

winsUser = 0
winsAI = 0

states = ['play', 'winUser', 'winAI', 'draw', 'stop']

current_state = ''


def main():

    while True:
        ask_play = input('Do you want to play? y/n: ')
        if ask_play == 'n':
            break
        if ask_play != 'y':
            print('Please enter y or n: ')
            continue
        count = 0
        while count<9:
            # user is 0
            if count %2 == 0:
                user_turn()
                if check_winner(0):
                    display_winner(0)
                    break
            # ai is 1
            else:
                ai_turn()
                if check_winner(1):
                    display_winner(1)
                    break
            count += 1
        if count == 9:
            display_draw()
        reset_board()


def print_board():
    for row in board:
        for entry in board[row].values():
            print('|', end='')
            if entry == 0:
                print(' X |', end='')
            elif entry == 1:
                print(' O |', end='')
            else:
                print('   |', end='')
        print('\n_______________\n')


def user_turn():
    print_board()
    valid = False
    while not valid:
        row = input('Input row of next move: ')
        column = input('Input column of next move: ')
        try:
            temp = board[int(row)][int(column)]
            if temp != -1:
                print('Choose empty entry')
                continue
            board[int(row)][int(column)] = 0
            valid = True
        except KeyError:
            print('Put valid inputs')
        except ValueError:
            print('Put valid inputs')


def input_ai_result(coordinates: tuple):
    if coordinates is None:
        return
    board[coordinates[0]][coordinates[1]] = 1


def ai_turn():
    tuple_to_input = ai_win_next_turn()
    if tuple_to_input is not None:
        input_ai_result(tuple_to_input)
        return
    tuple_to_input = user_win_next_turn()
    if tuple_to_input is not None:
        input_ai_result(tuple_to_input)
        return
    tuple_to_input = ai_win_in_two_turns()
    if tuple_to_input is not None:
        input_ai_result(tuple_to_input)
        return

    while(True):
        row = random.randint(0,2)
        column = random.randint(0,2)
        if board[row][column] == -1:
            board[row][column] = 1
            break


def ai_win_next_turn() -> tuple:
    result_check = checkColumns_win_next_turn(1)
    if result_check is not None:
        return result_check
    result_check = checkRows_next_turn(1)
    if result_check is not None:
        return result_check
    result_check = checkDiagonal_win_next(1)
    if result_check is not None:
        return result_check


def user_win_next_turn() -> tuple:
    result_check = checkColumns_win_next_turn(0)
    if result_check is not None:
        return result_check
    result_check = checkRows_next_turn(0)
    if result_check is not None:
        return result_check
    result_check = checkDiagonal_win_next(0)
    if result_check is not None:
        return result_check


def ai_win_in_two_turns() -> tuple :
    for row in board:
        for column in range(3):
            if board[row][column] == -1:
                board[row][column] = 1
                output = ai_win_next_turn()
                if output is not None:
                    board[row][column] = -1
                    return output
                board[row][column] = -1
                output = user_win_next_turn()
                if output is not None:
                    board[row][column] = -1
                    return output
                board[row][column] = -1


# noinspection PyRedundantParentheses
def checkRows_next_turn(player):
    for row in board:
        if board[row][0] == player and board[row][1] == player and board[row][2] == -1:
            return (row,2)
        if board[row][0] == player and board[row][1] == -1 and board[row][2] == player:
            return (row,1)
        if board[row][0] == -1 and board[row][1] == player and board[row][2] == player:
            return (row,0)


# noinspection PyRedundantParentheses
def checkColumns_win_next_turn(player) -> tuple:
    for column in range(0,3):
        if board[0][column] == player and board[1][column] == player and board[2][column] == -1:
            return (2,column)
        if board[0][column] == player and board[1][column] == -1 and board[2][column] == player:
            return (1,column)
        if board[0][column] == -1 and board[1][column] == player and board[2][column] == player:
            return (0,column)


# noinspection PyRedundantParentheses
def checkDiagonal_win_next(player):
    # check diagonal upper left to lower right
    if board[0][0] == player and board[1][1] == player and board[2][2] == -1:
        return (2,2)
    if board[0][0] == player and board[1][1] == -1 and board[2][2] == player:
        return (1,1)
    if board[0][0] == -1 and board[1][1] == player and board[2][2] == player:
        return (0,0)

    # check other diagonal
    if board[0][2] == player and board[1][1] == player and board[2][0] == -1:
        return (2,0)
    if board[0][2] == player and board[1][1] == -1 and board[2][0] == player:
        return (1,1)
    if board[0][2] == -1 and board[1][1] == player and board[2][0] == player:
        return (0,2)


def check_winner(player) -> bool:
    if checkRows_winner(player):
        return True
    if checkDiagonal_winner(player):
        return True
    if checkColumns_winner(player):
        return True
    return False


def checkColumns_winner(player) -> bool:
    for column in range(0,3):
        if board[0][column] == player and board[1][column] == player and board[2][column] == player:
            return True
        if board[0][column] == player and board[1][column] == player and board[2][column] == player:
            return True
        if board[0][column] == player and board[1][column] == player and board[2][column] == player:
            return True
    return False


def checkRows_winner(player) -> bool:
    for row in board:
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False


def checkDiagonal_winner(player):
    # check diagonal upper left to lower right
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    # check other diagonal
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True


def display_winner(player):
    global winsAI
    global winsUser
    if player == 1:
        winsAI += 1
        print('====== COMPUTER WON ======')

    else:
        winsUser += 1
        print('====== USER WON ======')
    print(f'    User wins :  {winsUser}\n'
          f'Computer wins :  {winsAI}')


def display_draw():
    print('====== DRAW ======')
    print(f'    User wins :  {winsUser}\n'
          f'Computer wins :  {winsAI}')


def reset_board():
    global board
    board = {
        0: {
            0: -1,
            1: -1,
            2: -1,
        },
        1: {
            0: -1,
            1: -1,
            2: -1,
        },
        2: {
            0: -1,
            1: -1,
            2: -1,
        },
    }


if __name__ == '__main__':
    main()
