def getBlankPosition(board):
    # Return the x and y of board coordinates of the blank space.    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if board[x][y] == BLANK:
                return (x, y)
