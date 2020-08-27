import numpy as np
import sys
# print (np.matrix(board.sudoku))
class board(object):
    def __init__(self):
        board.sudoku = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,5,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]
    #I created this function in order to reset the quadrant position within the board.sudoku board.sudoku.
    #Explained in docs

    def calculatePosition(self,number):
        return (number//3)*3

    def isGameOver(self):
        for x in range(9):
            for y in range(9):
                if board.sudoku[x][y] == 0:
                    return False
        return True
        
       
    def setNumber(self,coordX,coordY,number):
        board.sudoku[coordX][coordY] = number
        # print('Move set at %2d,%2d',coordX,coordY)
    
    def possibleMove(self,y,x,n):
        for i in range(0,9):
            if board.sudoku[x][i]==n:
                # print('number in row')
                return False
        
        for i in range(0,9):
            if board.sudoku[i][y]==n:
                # print('number in column')
                return False
       
        y0 = self.calculatePosition(y)
        x0 = self.calculatePosition(x)

        for i in range(0,3):
            for j in range(0,3):
                if board.sudoku[y0+i][x0+j] == n:
                    # print('number in quadrant')
                    return False
        # print('number not present')
        return True
        
    def solve(self):
            for y in range(9):
                for x in range(9):
                    if board.sudoku[x][y] == 0:
                        for n in range(1,10):                    
                            if self.possibleMove(y,x,n):
                                board.sudoku[y][x] = n
                                self.solve()
                                board.sudoku[y][x] = 0
                        return
        
    def printBoard(self):
        print(np.matrix(board.sudoku))

class game:
    def __init__(self):
        pass

    def main():
        sys.setrecursionlimit(100000000)
        gameBoard = board()
        gameBoard.solve()
        gameBoard.printBoard()



    if __name__ == '__main__':
        main()
           