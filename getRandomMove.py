def getRandomMove(board, lastMove=None):
    # start with a full list of all four moves    validMoves = [UP, DOWN, LEFT, RIGHT]

    # remove moves from the list as they are disqualified    if lastMove == UP or not isValidMove(board, DOWN):
        validMoves.remove(DOWN)
    if lastMove == DOWN or not isValidMove(board, UP):
        validMoves.remove(UP)
    if lastMove == LEFT or not isValidMove(board, RIGHT):
        validMoves.remove(RIGHT)
    if lastMove == RIGHT or not isValidMove(board, LEFT):
        validMoves.remove(LEFT)

    # return a random move from the list of remaining moves    return random.choice(validMoves)