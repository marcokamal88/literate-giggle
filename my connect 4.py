# marco kamal
# ID=20210311
# game=coneect 4

BOARD_COLS = 7
BOARD_ROWS = 6
from operator import truediv
import numpy as np
# creating board
def creat_board():
    board=np.zeros((BOARD_ROWS,BOARD_COLS))
    return board
# rules of the game 
    # dropping down
def drop_piece(board,col,row,piece):
    board[row][col]=piece
    # check if the location is valid
def is_valid_location(board,col):
    return board[5][col]==0
    # going to the next open row
def get_next_open_row(board,col):
    for r in range(6):
        if board[r][col]==0:
            return r
def print_board(board):
    print(np.flip(board,0))
    # checking if there  is winnier
def winning_check(board ,piece):
    # check horizontal locations for winning 
    for c in range(BOARD_COLS-3):
        for r in range(BOARD_ROWS):
            if board[r][c]==piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece:
                return True
    # check virtical locations for winning 
    for c in range(BOARD_COLS):
        for r in range(BOARD_ROWS-3):
            if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece:
                return True
    # check sloped diagenals +
    for c in range(BOARD_COLS-3):
        for r in range(BOARD_ROWS-3):
            if board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
                return True
    # check sloped diagenals -
    for c in range(BOARD_COLS-3):
        for r in range(3,BOARD_ROWS):
            if board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
                return True
board=creat_board()
print_board(board)
game_over=False
turn=0
while not game_over:
# asking for p1 input 
    if turn==0:
        col=int(input("p1: choose a num(0-6): "))
        if is_valid_location(board,col):
            row=get_next_open_row(board,col)
            drop_piece(board,col,row,1)
            if winning_check(board,1):
                print("the winner is player 1!! congrat!")
                game_over=True

# asking p2 for input
    else:
        col=int(input("p2: choose a num(0-6): "))
        if is_valid_location(board,col):
            row=get_next_open_row(board,col)
            drop_piece(board,col,row,2)
    print_board(board)
    if winning_check(board,2):
                print("the winner is player 2 !! congrat!")
                game_over=True
                break
    turn+=1
    turn=turn%2