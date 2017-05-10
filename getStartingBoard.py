def getStartingBoard():
    ''' Return a board data structure with tiles in the solved state.    For example, if BOARDWIDTH and BOARDHEIGHT are both 3, this function    returns [[1, 4, 7], [2, 5, 8], [3, 6, BLANK]]'''    counter = 1    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(counter)
            counter += BOARDWIDTH
        board.append(column)
        counter -= BOARDWIDTH * (BOARDHEIGHT - 1) + BOARDWIDTH - 1
    board[BOARDWIDTH-1][BOARDHEIGHT-1] = BLANK
    return board