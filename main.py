import numpy as np
import pygame as py 

# print (np.matrix(sudoku))
class board(object):
    
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
        print('Move set at %2d,%2d',coordX,coordY)

    def inColumn(self,number,columnIndex):
        for num in range(len(board.matrix[columnIndex])):
            if number == (board.matrix[num][columnIndex]):
                print('Number already present in column')
                return True
        return False
        

    def inRow(self,number,rowIndex):
        for num in range(len(board.matrix[rowIndex])):
            if number == (board.matrix[rowIndex][num]):
                print('Number already present in row')
                return True
        return False
        

    def inQuadrant(self,number,coordX,coordY):
        coordX = self.calculatePosition(coordX)
        coordY = self.calculatePosition(coordY)
        print(self.calculatePosition(coordX))
        print(self.calculatePosition(coordY))
        for x in range(coordX,coordX+3):
            for y in range(coordY,coordY+3):
                if number == board.matrix[coordX][coordY]:
                    print('Number already exists in that quadrant')
                    return True
        return False           
    
    def moveCanOccur(self,number,coordX,coordY):
        return not self.inQuadrant(number,coordX,coordY) and not self.inRow(number,coordX) and not self.inColumn(number,coordY)


#I created this function in order to reset the quadrant position within the sudoku board.
#Explained in docs
    def calculatePosition(self,number):
        while number % 3 != 0:
            number-=1
        return number
    
class game:
    def __init__(self):
        pass

    def main():
        dimensions = 9
        gameboard = board(dimensions)
        while not gameboard.isGameOver():
            while True:
                print(np.matrix(gameboard.matrix))
                row = int(input('Enter the X Coordinate: '))
                col = int(input('Enter the Y coordinate: '))
                num = int(input('Enter the number: '))
                if gameboard.moveCanOccur(num,row,col):
                    gameboard.setNumber(row,col,num)
                    break
                else:
                    print('Error , Try again')


    if __name__ == '__main__':
        main()
           