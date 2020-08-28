b = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7] 
]

def empty_pos(b):
    for x in range(len(b)):
        for y in range(len(b[0])):
            if b[x][y] == 0:
                return [x,y]
    return None

def valid_move(b,num,coords):
    for j in range(9):
        if num == b[coords[0]][j]:
            return False
        
    for j in range(9):
        if num == b[j][coords[1]]:
            return False
            
    coordx = isolate_position(coords[1])
    coordy = isolate_position(coords[0])

    for i in range(coordy, coordy + 3):
        for j in range(coordx, coordx + 3):
            if b[i][j] == num:
                return False      
    return True

def isolate_position(num):
    while num %3 != 0:
        num = num-1
    return num
        
def print_board(b):
    print("---------------------") 
    for z in range(9):
        if z % 3 == 0 and z != 0:
            print("---------------------") 

        for q in range(9):
            if q % 3 == 0 and q != 0:
                print("|", end="")

            if q == 8:
                print(b[z][q])
            else:
                print(str(b[z][q]) + " ", end="")

    print("---------------------")        
    
def solve(b):
    empty = empty_pos(b)
    if not empty:
        print('\n Solved:')
        print_board(b)
        return True
    else:
        posX,posY = empty_pos(b)
        for n in range(1,10):
            if valid_move(b,n,(posX,posY)):
                b[posX][posY]=n
                if solve(b):
                    return True
                b[posX][posY]=0
    return False


print_board(b)
solve(b)