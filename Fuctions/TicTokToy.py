import os
import time
import random

board=[""," "," "," "," "," "," "," "," "," "]# if we give less spaces it will show array out of bound exception,This space is used to allocate the memory
def print_board():
    print("print the elements 0-8.....")
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " ")#if we give same numbers for every board then if we enter one elemets it will take to all other elements..
    print("___|___|___")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("___|___|___")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")
    print("   |   |   ")

while True :
    print_board()
    choice=int(input("enter an empty sapce for X:"))
    if board[choice]==" ":#check weather board of choice is x or not
        board[choice]='X'#board of choice is x thn replace space with X
    else:
        print("space is already filled...")
        #check fo x win

    if      board[1]=='X' and board[2]=='X' and board[3]=='X' or \
            board[4] == 'X' and board[5] == 'X' and board[6] == 'X' or \
            board[7] == 'X' and board[8] == 'X' and board[9] == 'X' or \
            board[1] == 'X' and board[3] == 'X' and board[5] == 'X' or \
            board[2] == 'X' and board[3] == 'X' and board[6] == 'X' or \
            board[3] == 'X' and board[6] == 'X' and board[9] == 'X' or \
            board[3] == 'X' and board[5] == 'X' and board[7] == 'X' or \
            board[1] == 'X' and board[3] == 'X' and board[9] == 'X' :
            print_board()
            print("X wins congratulations....")
            break

        #get player o input

#
    choice=int(input("select empty space for O..."))
    if board[choice]==" ":
        board[choice]='O'
    else:
        print("space is already filled....")
        time.sleep(1)
    print_board()
    #player o choice...
    if      board[1]=='O  ' and board[2]=='O' and board[3]=='O' or \
            board[4] == 'O' and board[5] == 'O' and board[6] == 'O' or \
            board[7] == 'O' and board[8] == 'O' and board[9] == 'O' or \
            board[1] == 'O' and board[3] == 'O' and board[5] == 'O' or \
            board[2] == 'O' and board[3] == 'O' and board[6] == 'O' or \
            board[3] == 'O' and board[6] == 'O' and board[9] == 'O' or \
            board[3] == 'O' and board[5] == 'O' and board[7] == 'O' or \
            board[1] == 'O' and board[3] == 'O' and board[9] == 'O' :
            os.system("clear")
            print_board()
            print("O wins congratulations.....")
            break
'''def check_for_tie():
    isfull=True
    if " " in board:#if there is a space in the board
        isfull=False
    else:
        isfull=True
        #if board is full...
    if isfull==True:
        print("Tie......")'''

