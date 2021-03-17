
def get_neighbors(board,coords,boardendcoords):
    #printboard(board)
    adjacentNodes = []
    for i in range(-1,2):
        for j in range(-1,2):
            if abs(i + j) == 1:
                var1 = coords[0] + i
                var2 = coords[1] + j
                if 0 <= var1 < boardendcoords[0] and 0 <= var2 < boardendcoords[1] and board[var1][var2] == 0:
                        adjacentNodes.append((var1,var2))
    '''for i in range(-1,2,2):
        var = coords[0] + i
        if var >= 0 and var < boardendcoords[0] and board[var][coords[1]] == 0 and (var,coords[1]) not in visited:
            adjacentNodes.append((var,coords[1]))

    for i in range(-1,2,2):
        var = coords[1] + i
        if var >= 0 and var < boardendcoords[1] and board[coords[0]][var] == 0 and (coords[0],var) not in visited:
            adjacentNodes.append((coords[0],var))'''

    return adjacentNodes

def pathfind(origins,start,end):
    node = end
    if node not in origins:
        return
    path = [end]
    while True:
        if node == start:
            return path
        path.append(origins[node])
        node = origins[node]

def bfs(board,start,end):
    boardendcoords = (len(board),(len(board[0])))
    queue = [start]
    visited = [start]
    origins  = {start:start}
    while queue:
        node = queue.pop(0)
        #print(node)

        if node == end:
            #print('nice',origins,start,end)
            return [x for x in visited if x not in queue],queue,pathfind(origins,start,end)

        neighbors = get_neighbors(board,node,boardendcoords)
        for neighbor in neighbors:
            if neighbor not in visited:
                origins[neighbor] = node
                visited.append(neighbor)
                queue.append(neighbor)

    #print(origins,'\n',visited,pathfind(origins,start,end))
    print('No path found')
    return visited,queue,[]

'''board = [
    [0,0],
    [0,0],
]'''
'''board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]
start = (0,0)
end = (2,2)
print(bfs(board,start,end))'''
