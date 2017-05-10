def drawTile(tilex, tiley, number, adjx=0, adjy=0):
    '''Draw a tile at board coordinates tilex and tiley, optionally a few    pixels over (determined by adjx and adjy)'''    left, top = getLeftTopOfTile(tilex, tiley)
    pygame.draw.rect(DISPLAYSURF, TILECOLOR, (left + adjx, top + adjy, TILESIZE, TILESIZE))
    textSurf = BASICFONT.render(str(number), True, TEXTCOLOR)
    '''textSurf = pygame.image.load("yano1.png").convert_alpha()'''    textRect = textSurf.get_rect()
    textRect.center = left + int(TILESIZE / 2) + adjx, top + int(TILESIZE / 2) + adjy
    DISPLAYSURF.blit(textSurf, textRect)