
'''def printboard(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            print(board[y][x], end = " ")
        print()
'''
def extendborder(border,boardendcoords):
    for i in range(2):
        if border[0][i] != 0:
            border[0][i] -= 1

    for i in range(2):
        if border[1][i] != boardendcoords[i]:
            border[1][i] += 1
    return border

def incrementnodes(board,border):
    for y in range(border[0][0],border[1][0]+1):
        for x in range(border[0][1],border[1][1]+1):
            if board[y][x] > 0:
                board[y][x] += 1
    return board

def addnodes(board,coords,boardendcoords):
    #printboard(board)
    for i in range(-1,2,2):
        var = coords[0] + i
        if var >= 0 and var <= boardendcoords[0]:
            if board[var][coords[1]] == 0:
                board[var][coords[1]] += 1

    for i in range(-1,2,2):
        var = coords[1] + i
        if var >= 0 and var <= boardendcoords[1]:
            if board[coords[0]][var] == 0:
                board[coords[0]][var] += 1

    return board

def findOnes(board,border):
    for y in range(border[0][0],border[1][0]+1):
        for x in range(border[0][1],border[1][1]+1):
            if board[y][x] == 1:
                return True
    return False

def FindPath(endcoords,startcoords,board,boardendcoords):
    coords = endcoords[:]
    Value = board[endcoords[0]][endcoords[1]]
    newcoords = coords[:]
    PathFind = []
    while True:
        coords = newcoords[:]
        PathFind.append(coords)
        if coords == startcoords:
            return PathFind
        for i in range(-1,2,2):
            var = coords[0] + i
            if var >= 0 and var <= boardendcoords[0]:
                if board[var][coords[1]] > Value:
                    Value = board[var][coords[1]]
                    newcoords = [var,coords[1]]

        for i in range(-1,2,2):
            var = coords[1] + i
            if var >= 0 and var <= boardendcoords[1]:
                if board[coords[0]][var] > Value:
                    Value = board[coords[0]][var]
                    newcoords = [coords[0],var]

def bfs(startcoords,endcoords,initboard):#,maxdepth=1
    board = [x[:] for x in initboard]
    board[startcoords[0]][startcoords[1]] = 1
    #board[endcoords[0]][endcoords[1]] = 2
    boardendcoords = [len(board)-1,len(board[0])-1]
    #board[boardendcoords[0]][boardendcoords[1]] = 1
    #printboard(board);print()
    border = [list(startcoords),list(startcoords)]

    end = False
    #find = False
    i = 0
    while not end:
        i += 1
        board = incrementnodes(board,border)
        border = extendborder(border,boardendcoords)
        for y in range(border[0][0],border[1][0]+1):
            for x in range(border[0][1],border[1][1]+1):
                if board[y][x] == 2:
                    board = addnodes(board,[y,x],boardendcoords)
        #printboard(board);print()
        if board[endcoords[0]][endcoords[1]] >= 1:
            end = True
            #print('end')
        if i%100 == 0:
            print('check',i)
            if findOnes(board,border) == False:
                print('Cannot Find End')
                return board,[]

    '''board[border[0][0]][border[0][1]] = 'A'
    board[border[1][0]][border[1][1]] = 'B'
    '''
    PathFind = FindPath(endcoords,startcoords,board,boardendcoords)
    print('border:',border,'PathFind:',PathFind)
    return board,PathFind
############################################
#sleep(5)
#grid2[0][0] = 1
'''printboard(grid)
grid2 = bfs([3,3],[0,0],grid)
printboard(grid)
printboard(grid2)'''