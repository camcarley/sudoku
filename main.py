import numpy as np

# print (np.matrix(sudoku))
class board:

    def isGameOver(self):
        for x in range(len(board.matrix)):
            for y in range(len(board.matrix[x])):
                if board.matrix[x][y] == 0:
                    return False
        return True

    def __init__(self,dimensions):
        board.matrix = [[0 for i in range(dimensions)] for j in range(dimensions)]

    def setNumber(self,coordX,coordY,number):
        board.matrix[coordX][coordY] = number

    def inColumn(self,number,columnIndex):
        for num in range(len(board.matrix[columnIndex])):
            if number == (board.matrix[num][columnIndex]):
                return True
        return False
        

    def inRow(self,number,rowIndex):
        for num in range(len(board.matrix[rowIndex])):
            if number == (board.matrix[rowIndex][num]):
                return True
        return False
        

    def inQuadrant(self,number,coordX,coordY):
        coordX = calculatePosition(coordX)
        coordY = calculatePosition(coordY)
        for x in range(coordX,coordX+3):
            for y in range(coordY,coordY+3):
                if number == board.matrix[coordX][coordY]:
                    return False
        return True            
    
    def checkMove(self,number,coordX,coordY):
        return inQuadrant(number,coordX,coordY) and inRow(number,coordX) and inColumn(number,coordY)


#I created this function in order to reset the quadrant position within the sudoku board.
#Explained in docs
    def calculatePosition(self,number):
        while number % 3 != 0:
            number-=1
        return number
        


class game:
    if __name__ == '__main__':
    #   dimensions = int(input("What board size would you like to play with?"))
            dimensions = 9
            fun = board(dimensions)
            while(fun.isGameOver() == False):
                col = int(input('Which column do you want to enter the number?'))
                row = int(input('Enter the X Coordinate'))
                num = int(input('Enter the Y Coordinate'))
                fun.setNumber(row,col,num)
                print(np.matrix(board.matrix))