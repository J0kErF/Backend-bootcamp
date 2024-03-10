class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[0 for i in range(cols)] for j in range(rows)]
        
    def get_cell(self, row, col):
        return self.board[row][col]
    def set_cell(self, row, col, state):
        self.board[row][col] = state

    def get_neighbors(self, row, col):
        # these are the 8 neighbors of a cell that we need to check
        # X X X
        # X O X
        # X X X

        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                #these three ifs are to check if the cell is out of the board
                if i == 0 and j == 0:
                    # this if to skip the cell itself 
                    continue
                if row + i < 0 or row + i >= self.rows:
                    # this if to check if the cell is out of the board rows
                    continue
                if col + j < 0 or col + j >= self.cols:
                    # this if to check if the cell is out of the board cols
                    continue

                neighbors.append(self.get_cell(row + i, col + j))
        return neighbors
    
    def update(self):

        # to make it easier to manipulate the board I created a new board also not to mess up the current board for the other cells 
        new_board = [[0 for i in range(self.cols)] for j in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):

                # getting all the neighbors of the cell 
                neighbors = self.get_neighbors(i, j)
                # getting the number of live neighbors by sum function because 1 represents live cell and 0 represents dead cell
                live_neighbors = sum(neighbors)

                if self.get_cell(i, j) == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        # 1'st condition and 3'rd condition
                        new_board[i][j] = 0
                    else:
                        # 2'nd condition
                        new_board[i][j] = 1
                else:
                    # 4'th condition
                    if live_neighbors == 3:
                        new_board[i][j] = 1
        # update the new board state         
        self.board = new_board
