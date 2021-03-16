import pygame
import random
from pathfind import bfs
from time import time
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
#GRAY = (112,128,144)
#PURPLE = (255,0,255)
ORANGE = (255,165,0)
WIDTH = 30
LineWidth = 5
MARGIN = 1
CELLS_X = 25
CELLS_Y = 35

Start = (0,0)
End = (0,0)
ToggleStartEnd = True
UserDraw = False
ClickVal = 0
#ToggleWallVoid = True
FRAMES = 60
ShowFPS = False
PathFind = []
OpenNodes = []
ClosedNodes = []
# board default varible
Board_VAL = 0

board = [[Board_VAL for x in range(CELLS_Y)] for y in range(CELLS_X)]

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [(WIDTH + MARGIN) * CELLS_Y + MARGIN,
               (WIDTH + MARGIN) * CELLS_X + MARGIN]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("BFS pathfinding")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", WIDTH // 2)
def Text(row, column):
    info = str(board[row][column])
    num_text = font.render(info, 1, pygame.Color("coral"))
    return num_text

'''def RemovePath(board):
    for i in range(len(board)):
        board[i] = [0 if x>0 else x for x in board[i]]
    return board
'''
def MouseToMatrix():
    pos = pygame.mouse.get_pos()
    #print(pos)
    column = (pos[0]-1) // (WIDTH + MARGIN)
    row = (pos[1]-1) // (WIDTH + MARGIN)
    return column,row

def eventDetect():
    global done,Start,End,ToggleStartEnd,UserDraw,board,ClickVal,PathFind,ClosedNodes, OpenNodes

    if event.type == pygame.QUIT:
        done = True

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            row,column = MouseToMatrix()
            #print(column,row)
            if ToggleStartEnd:
                Start = (column,row)
            else:
                End = (column,row)

        elif event.button == 2:
            ToggleStartEnd = not ToggleStartEnd

        elif event.button == 3:
            UserDraw = True
            column,row = MouseToMatrix()
            #print(column,row)
            if board[row][column] >= 0:
                board[row][column] = -1
            else:
                board[row][column] = 0
            ClickVal = board[row][column]

    if event.type == pygame.MOUSEBUTTONUP:
        UserDraw = False

    if event.type == pygame.MOUSEMOTION:
        if UserDraw:
            column,row = MouseToMatrix()
            board[row][column] = ClickVal

    if event.type == pygame.KEYDOWN:

        '''if event.key == pygame.K_2:
            print('ToggleWallVoid',ToggleWallVoid)
            ToggleWallVoid = not ToggleWallVoid'''

        if event.key == pygame.K_x:
            RandLoops = int((len(board)*len(board[0]))**0.5)
            for x in range(RandLoops):
                RandX = random.randint(0,len(board)-1)
                RandY = random.randint(0,len(board[0])-1)
                board[RandX][RandY] = -1

        elif event.key == pygame.K_LSHIFT:
            board = [[Board_VAL for x in range(CELLS_Y)] for y in range(CELLS_X)]
            #board = RemovePath(board)
            PathFind = []
            OpenNodes = []
            ClosedNodes = []

        elif event.key == pygame.K_LCTRL:
            #board = [[Board_VAL for x in range(CELLS_Y)] for y in range(CELLS_X)]
            #board = RemovePath(board)
            PathFind = []
            OpenNodes = []
            ClosedNodes = []

        elif event.key == pygame.K_SPACE:
            #board = RemovePath(board)
            t0 = time()
            ClosedNodes, OpenNodes, PathFind = bfs(board,Start,End)
            t1 = time()
            PathFind = ConvertPath(PathFind)
            t2 = t1 - t0
            print('Time Taken:',t2)

def ConvertPath(PathFind):
    NewPath = []
    for Step in PathFind:
        Step1 = list(Step[::-1])
        for i in range(2):
            Step1[i] = (MARGIN + WIDTH) * Step1[i] + MARGIN + WIDTH // 2
        NewPath.append(tuple(Step1))
    return NewPath

def DrawStartEnd():
    pygame.draw.circle(screen, GREEN,
    [(MARGIN + WIDTH) * Start[1] + MARGIN + WIDTH // 2,
    (MARGIN + WIDTH) * Start[0] + MARGIN + WIDTH // 2], WIDTH // 2)

    pygame.draw.circle(screen, RED,
    [(MARGIN + WIDTH) * End[1] + MARGIN + WIDTH // 2,
    (MARGIN + WIDTH) * End[0] + MARGIN + WIDTH // 2], WIDTH // 2)

def DrawPath():
    '''
    #Draw a circle path
    for Step in PathFind:
        pygame.draw.circle(screen, GRAY,
        [(MARGIN + WIDTH) * Step[1] + MARGIN + WIDTH // 2,
        (MARGIN + WIDTH) * Step[0] + MARGIN + WIDTH // 2], WIDTH // 2)'''
    if len(PathFind) > 1:
        pygame.draw.lines(screen, ORANGE, False, PathFind, LineWidth)

'''def DrawNodes():
    for node in ClosedNodes:
        pygame.draw.rect(screen, BLUE,
            [(MARGIN + WIDTH) * node[1] + MARGIN,
            (MARGIN + WIDTH) * node[0] + MARGIN, WIDTH, WIDTH])
    for node in OpenNodes:
        pygame.draw.rect(screen, GREEN,
            [(MARGIN + WIDTH) * node[1] + MARGIN,
            (MARGIN + WIDTH) * node[0] + MARGIN, WIDTH, WIDTH])'''

def DrawGrid():
    for row in range(CELLS_X):
        for column in range(CELLS_Y):
            color = WHITE
            if board[row][column] != 0:# board[row][column] < 0:
                color = BLACK
            elif (row,column) in OpenNodes:
                color = GREEN
            elif (row,column) in ClosedNodes:
                color = BLUE
            '''elif board[row][column] == 0:
                color = WHITE'''

            pygame.draw.rect(screen, color,
                [(MARGIN + WIDTH) * column + MARGIN,
                (MARGIN + WIDTH) * row + MARGIN, WIDTH, WIDTH])

            #screen.blit(Text(row,column), ((MARGIN + WIDTH) * column + MARGIN, (MARGIN + WIDTH) * row + MARGIN))

def Render():
    screen.fill(BLACK)

    DrawGrid()
    #DrawNodes()
    DrawStartEnd()
    DrawPath()
    #pygame.draw.lines(screen, (255,0,255), False, [(20,20), (70,80),(255,0)], 2)
#--------------------------------------------------------#

while not done:
    for event in pygame.event.get():
        eventDetect()

    # Draw the board
    Render()

    # Limit to x frames per second
    clock.tick(FRAMES)
    #update screen
    pygame.display.flip()
#--------------------------------------------------------#
pygame.quit()
