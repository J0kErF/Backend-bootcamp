from board import Board
import utils

class Game:
    def __init__(self, rows, cols):
        self.board = Board(rows, cols)
    def populate_board(self):

        user_input = utils.get_user_input("Enter the index of live cell (<8,8> board from 1 to 8) 'row,col' and anything else to end: ")
        
        while utils.check_coordinates(user_input) != False:
            

            row, col = user_input.split(",")
            row = int(row)-1
            col = int(col)-1
            self.board.set_cell(row, col, 1)

            user_input = utils.get_user_input("Enter the next index of the live cell in the same format or anything else to end: ")

    def run_simulation(self, num_rounds):
        for i in range(num_rounds):
            self.board.update()
            utils.clear_screen()
            utils.print_board(self.board)
            utils.wait_seconds(1)
            print()
    