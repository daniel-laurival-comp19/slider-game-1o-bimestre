def makeText(text, color, bgcolor, top, left):
    # create the Surface and Rect objects for some text.    textSurf = BASICFONT.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)
