import os
clear = lambda: os.system('cls')


def display_board(board):
    clear

    print('       |       |       ')
    print('  ' + board[1] + '    |   ' + board[2] + '   |   ' + board[3] + '   ')
    print('       |       |       ')
    print('-----------------------')
    print('       |       |       ')
    print('  ' + board[4] + '    |   ' + board[5] + '   |   ' + board[6] + '   ')
    print('       |       |       ')
    print('-----------------------')
    print('       |       |       ')
    print('  ' + board[7] + '    |   ' + board[8] + '   |   ' + board[9] + '   ')
    print('       |       |       ')


def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input("\n\nPlayer 1:" + " Please enter your mark ".upper() + "('X' or 'O'): ").upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')



def place_marker(board, marker, position):
    os.system('cls')
    board[position] = marker


def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[7] == mark and board[8] == mark and board[9] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    return board[position] == '1' or board[position] == '2' or board[position] == '3' or board[position] == '4' or board[position] == '5' or board[position] == '6' or board[position] == '7' or board[position] == '8' or board[position] == '9'


def full_board_check(board):
    for temp in range(1, 10):
        if space_check(board, temp):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

def logo():
    print("\n        ##############  ####      ########          ##############       ######           ########   ")
    print("        ##############  ####    ###########         ##############    ############      ###########  ")
    print("             ####             ####       ###             ####        #####    #####   ####       ### ")
    print("             ####       ####  ####                       ####       ####        ####  ####           ")
    print("             ####       ####  ####                       ####       ################  ####           ")
    print("             ####       ####  ####       ###             ####       ################  ####       ### ")
    print("             ####       ####    ###########              ####       ####        ####    ###########  ")
    print("             ####       ####     #########               ####       ####        ####     #########   ")

    print("\n                                ##############      #######     ###########                          ")
    print("                                ##############    ##########    ###########                          ")
    print("                                     ####       ####      ####  ####                                 ")
    print("                                     ####       ####      ####  #######                              ")
    print("                                     ####       ####      ####  #######                              ")
    print("                                     ####       ####      ####  ####                                 ")
    print("                                     ####         ##########    ###########                          ")
    print("                                     ####          ########     ###########                          ")




logo()
while True:

    playBoard = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('\nAre you ready to play? [Y/N] ')

    if play_game.lower()[0] == 'y':
        os.system('cls')
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':

            display_board(playBoard)
            position = player_choice(playBoard)
            place_marker(playBoard, player1_marker, position)

            if win_check(playBoard, player1_marker):
                display_board(playBoard)
                print('Congratulations! Player 1 have WON the GAME!!!')
                game_on = False

            else:
                if full_board_check(playBoard):
                    display_board(playBoard)
                    print('The game is a DRAW!')
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(playBoard)
            position = player_choice(playBoard)
            place_marker(playBoard, player2_marker, position)

            if win_check(playBoard, player2_marker):
                display_board(playBoard)
                print('Congratulations! Player 2 have WON the GAME!!!')
                game_on = False
            else:
                if full_board_check(playBoard):
                    display_board(playBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
