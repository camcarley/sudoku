import numpy as np
# print (np.matrix(sudoku))

class board(object):
    
    def __init__(self):
        board.matrix = [
            [7,8,0,4,0,0,1,2,0],
            [6,0,0,0,7,5,0,0,9],
            [0,0,0,6,0,1,0,7,8],
            [0,0,7,0,4,0,2,6,0],
            [0,0,1,0,5,0,9,3,0],
            [9,0,4,0,6,0,0,0,5],
            [0,7,0,3,0,0,0,1,2],
            [1,2,0,0,0,7,4,0,0],
            [0,4,9,2,0,6,0,0,7]]


    def empty_pos(self):
        for x in range(9):
            for y in range(9):
                if board.matrix[x][y] == 0:
                    print((x,y))
                    return (x,y)
        return None

    def in_column(self,num,col):
        for n in range(9):
            if num == board.matrix[n][col]:
                print('Number already present in column')
                return True
        return False
        

    def in_row(self,num,row):
        for n in range(9):
            if num == board.matrix[row][n]:
                print('Number already present in row')
                return True
        return False
        

    def in_quadrant(self,num,x,y):
        posx = self.isolate_position(x)
        posy = self.isolate_position(y)
        for x in range(posx,posx+3):
            for y in range(posy,posy+3):
                if num == board.matrix[y][x]:
                    print('Number already exists in that quadrant')
                    return True
        return False           
    
    def valid_move(self,num,y,x):
        if self.in_row(num,x):
            print('a')
            return False
        
        if self.in_row(num,y):
            print('b')
            return False

        if self.in_quadrant(num,x,y):
            print('c')
            return False

        return True
        
        
    def print_board(self):
        for z in range(len(board.matrix)):
            if z % 3 == 0 and z != 0:
                print("- - - - - - - - - - - - - ")

            for q in range(len(board.matrix[0])):
                if q % 3 == 0 and q != 0:
                    print("|", end="")

                if q == 8:
                    print(board.matrix[z][q])
                else:
                    print(str(board.matrix[z][q]) + " ", end="")
    
#I created this function in order to reset the quadrant position within the sudoku board.
#Explained in docs
    def isolate_position(self,num):
        return int((num/3)*3)

    def solve(self):
        find = self.empty_pos()
        if not find:
            return True
        else:
            posX,posY = find
            for n in range(1,10):
                if board.matrix[posY][posX]==0:
                    if self.valid_move(n,posY,posX):
                        board.matrix[posY][posX]=n
                        if self.solve():
                            return True
                        board.matrix[posY][posX]=n
            return False

    
class game:
    def __init__(self):
        pass

    def main():
        gameboard = board()
        print(np.matrix(gameboard.matrix))
        gameboard.solve()
        gameboard.print_board()


    if __name__ == '__main__':
        main()