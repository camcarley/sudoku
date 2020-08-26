import numpy as np

# print (np.matrix(sudoku))
class board(object):

    def isGameOver(self):
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == 0:
                    return False
        return True

    def __init__(self,dimensions):
        
        board = [[0 for i in range(dimensions)] for j in range(dimensions)]

    def setNumber(self,coordX,coordY,number):
        board[coordX][coordY] = number
        # print('Move set at %2d,%2d',coordX,coordY)

    def inColumn(self,number,columnIndex):
        for num in range(len(board[columnIndex])):
            if number == (board[num][columnIndex]):
                # print('Number already present in column')
                return True
        return False
        

    def inRow(self,number,rowIndex):
        for num in range(len(board[rowIndex])):
            if number == (board[rowIndex][num]):
                # print('Number already present in row')
                return True
        return False
        

    def inQuadrant(self,number,coordX,coordY):
        coordX = self.calculatePosition(coordX)
        coordY = self.calculatePosition(coordY)
        for x in range(coordX,coordX+3):
            for y in range(coordY,coordY+3):
                if number == board[coordX][coordY]:
                    # print('Number already exists in that quadrant')
                    return True
        return False           
    
    def isMovePossible(self,number,coordX,coordY):
        return not self.inQuadrant(number,coordX,coordY) and not self.inRow(number,coordX) and not self.inColumn(number,coordY)

    def solve(self):
        for x in range(9):
            for y in range(9):
                if board[x][y]==0:
                    for n in range(1,10):
                        if self.isMovePossible(n,x,y):
                            self.setNumber(x,y,n)
                            self.solve()
                            #If solution cannot complete , then backtracking will occur
                            self.setNumber(x,y,0)
                    return




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
        # while not gameboard.isGameOver():
        #     while True:
        #         print(np.matrix(gameboard))
        #         row = int(input('Enter the X Coordinate: '))
        #         col = int(input('Enter the Y coordinate: '))
        #         num = int(input('Enter the number: '))
        #         if gameboard.isMovePossible(num,row,col):
        #             gameboard.setNumber(row,col,num)
        #             break
        #         else:
        #             print('Error , Try again')
        gameboard.solve()
        print(np.matrix(gameboard))

    if __name__ == '__main__':
        main()
           