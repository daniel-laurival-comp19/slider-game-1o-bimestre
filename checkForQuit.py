def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events        terminate() # terminate if any QUIT events are present    for event in pygame.event.get(KEYUP): # get all the KEYUP events        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key        pygame.event.post(event) # put the other KEYUP event objects back
