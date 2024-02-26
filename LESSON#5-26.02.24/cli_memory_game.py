

import random


values= {'A':2,'car':2,'bag':2,'dog':2,'cat':2,3:2,2:2,1:2,4:2,5:2,6:2,7:2,8:2,9:2,0:2,10:2,'me':2,'run':2}
class point:
    def __init__(self, row,col, value):
        self.row = row
        self.col = col
        self.value = value
class board:
    
    def __init__(self, rows=6, cols=6,points=[]):
        self.rows = rows
        self.cols = cols
        self.points = points
        self.b= [[0 for i in range(cols)] for j in range(rows)]

    def generate_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                val=0
                while(values[val]<=0):
                    val=random.choice(list(values.keys()))
                values[val]-=1
                self.points.append(point(i,j,val))

    def print_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.b[i][j] == 0:
                    print("*",end=" ")
                else:
                    print(self.get_value(i,j),end=" ")
            print()

    def get_value(self,row,col):
        for p in self.points:
            if p.row==row and p.col==col:
                return p.value
        return None
    
    def show_value(self,row,col):
        self.b[row][col]=1
    def hide_value(self,row,col):
        self.b[row][col]=0

    def is_same(self,row1,col1,row2,col2):
        return self.get_value(row1,col1)==self.get_value(row2,col2)
    
    def is_done(self):
        for point in self.points:
            if self.b[point.row][point.col]==0:
                return False
        return True
    

b= board()
b.generate_board()
b.print_board()
#the game it self
while(b.is_done()==False):
    guess1=input("Enter the first guess: (row,col)")
    guess1=guess1.split(",")
    guess1[0]=int(guess1[0])
    guess1[1]=int(guess1[1])
    b.show_value(guess1[0],guess1[1])
    b.print_board()
    guess2=input("Enter the second guess: (row,col)")
    guess2=guess2.split(",")
    guess2[0]=int(guess2[0])
    guess2[1]=int(guess2[1])
    b.show_value(guess2[0],guess2[1])
    b.print_board()
    if b.is_same(guess1[0],guess1[1],guess2[0],guess2[1])==False:
        b.hide_value(guess1[0],guess1[1])
        b.hide_value(guess2[0],guess2[1])
        print("Try again")
    else:
        print("You found a pair")
    b.print_board()
print("You won")

    
