# Projeto de CES-22import pygame, sys, random
from pygame.locals import *

# Global constantsBOARDWIDTH = 4 # number of columns in the boardBOARDHEIGHT = 4 # number of rows in the boardTILESIZE = 80 # size of titleWINDOWWIDTH = 640WINDOWHEIGHT = 480FPS = 60 # frame per secondBLANK = None
# Color options#                 R    G    BBLACK =         (  0,   0,   0)
WHITE =         (255, 255, 255)
BRIGHTBLUE =    (  0,  50, 255)
DARKTURQUOISE = (  3,  54,  73)
GREEN =         (  0, 204,   0)

# Color in gameBGCOLOR = BLACK
TILECOLOR = DARKTURQUOISE
TEXTCOLOR = WHITE
BORDERCOLOR = GREEN
BASICFONTSIZE = 20
BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK
MESSAGECOLOR = WHITE

XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)

# ComandsUP = 'up'DOWN = 'down'LEFT = 'left'RIGHT = 'right'
def main():
    ''' Control the program '''
    global FPSCLOCK, DISPLAYSURF, BASICFONT, RESET_SURF, RESET_RECT, NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()   # FPS    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) # Display size    pygame.display.set_caption('Slide Puzzle') # Title    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE) # Font
    # Store the option buttons and their rectangles in OPTIONS.    RESET_SURF, RESET_RECT = makeText('Reset',    TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 90)
    NEW_SURF,   NEW_RECT   = makeText('New Game', TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 60)
    SOLVE_SURF, SOLVE_RECT = makeText('Solve',    TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 30)

    mainBoard, solutionSeq = generateNewPuzzle(80)
    SOLVEDBOARD = getStartingBoard() # a solved board is the same as the board in a start state.    allMoves = [] # list of moves made from the solved configuration
    while True: # main game loop        slideTo = None # the direction, if any, a tile should slide        msg = 'Click tile or press arrow keys to slide.' # contains the message to show in the upper left corner.        if mainBoard == SOLVEDBOARD:
            msg = 'Solved!'
        drawBoard(mainBoard, msg)

        checkForQuit()
        for event in pygame.event.get(): # event handling loop            if event.type == MOUSEBUTTONUP:
                spotx, spoty = getSpotClicked(mainBoard, event.pos[0], event.pos[1])

                if (spotx, spoty) == (None, None):
                    # check if the user clicked on an option button                    if RESET_RECT.collidepoint(event.pos):
                        resetAnimation(mainBoard, allMoves) # clicked on Reset button                        allMoves = []
                    elif NEW_RECT.collidepoint(event.pos):
                        mainBoard, solutionSeq = generateNewPuzzle(80) # clicked on New Game button                        allMoves = []
                    elif SOLVE_RECT.collidepoint(event.pos):
                        resetAnimation(mainBoard, solutionSeq + allMoves) # clicked on Solve button                        allMoves = []
                else:
                    # check if the clicked tile was next to the blank spot
                    blankx, blanky = getBlankPosition(mainBoard)
                    if spotx == blankx + 1 and spoty == blanky:
                        slideTo = LEFT
                    elif spotx == blankx - 1 and spoty == blanky:
                        slideTo = RIGHT
                    elif spotx == blankx and spoty == blanky + 1:
                        slideTo = UP
                    elif spotx == blankx and spoty == blanky - 1:
                        slideTo = DOWN

            elif event.type == KEYUP:
                # check if the user pressed a key to slide a tile                if event.key in (K_LEFT, K_a) and isValidMove(mainBoard, LEFT):
                    slideTo = LEFT
                elif event.key in (K_RIGHT, K_d) and isValidMove(mainBoard, RIGHT):
                    slideTo = RIGHT
                elif event.key in (K_UP, K_w) and isValidMove(mainBoard, UP):
                    slideTo = UP
                elif event.key in (K_DOWN, K_s) and isValidMove(mainBoard, DOWN):
                    slideTo = DOWN

        if slideTo:
            slideAnimation(mainBoard, slideTo, 'Click tile or press arrow keys to slide.', 8) # show slide on screen            makeMove(mainBoard, slideTo)
            allMoves.append(slideTo) # record the slide        pygame.display.update()
        FPSCLOCK.tick(FPS)