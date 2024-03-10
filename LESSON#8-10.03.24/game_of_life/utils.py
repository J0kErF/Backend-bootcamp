import os
import time
def clear_screen():
    os.system('clear')
def wait_seconds(seconds):
    time.sleep(seconds)
def print_board(board):
    for i in range(board.rows):
        for j in range(board.cols):
            if board.get_cell(i, j) == 1:
                print("X", end=" ")
            else:
                print(".", end=" ")
        print()
def get_user_input(message):
    return input(message)

def check_coordinates(input):
    if input == None:
        return False
    if input.count(",") != 1:
        return False
    if len(input.split(",")) != 2:
        return False
    if input.split(",")[0].isdigit() == False or input.split(",")[1].isdigit() == False:
        return False
    if input.split(",")[0] > "8" or input.split(",")[1] > "8":
        return False
    if input.split(",")[0] < "1" or input.split(",")[1] < "1":
        return False
    return True