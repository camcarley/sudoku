import numpy as np

# print (np.matrix(sudoku))
class board:

    def __init__(self,dimensions):
        board.matrix = [[0 for i in range(dimensions)] for j in range(dimensions)]
        pass

    def inColumn(self,number,columnIndex):
        for num in range(len(board.matrix[columnIndex])):
            if number == (board.matrix[num][columnIndex]):
                return True
        return False
        pass

    def inRow(self,number,rowIndex):
        for num in range(len(board.matrix[rowIndex])):
            if number == (board.matrix[rowIndex][num]):
                return True
        return False
        pass

    def inQuadrant(self, quadrantIndex):

        pass

class game:
    if __name__ == '__main__':
    #   dimensions = int(input("What board size would you like to play with?"))
        dimensions = 9
        fun = board(dimensions)
        # print('Hello World')
        print(np.matrix(board.matrix))
        print(board.inRow(0,1,0))
