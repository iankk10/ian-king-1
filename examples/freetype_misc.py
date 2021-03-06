import sys, os
import pygame
from pygame.locals import *

try:
    import pygame.freetype as freetype
except ImportError:
    print ("No FreeType support compiled")
    sys.exit ()

colors = {
    "grey_light"    :   pygame.Color(200, 200, 200),
    "grey_dark"     :   pygame.Color(100, 100, 100),
    "green"         :   pygame.Color(50, 255, 63),
    "red"           :   pygame.Color(220, 30, 30),
    "blue"          :   pygame.Color(50, 75, 245)
}

def run():
    pygame.init()

    fontdir = os.path.dirname(os.path.abspath (__file__))
    font = freetype.Font(os.path.join (fontdir, "data", "sans.ttf"))

    screen = pygame.display.set_mode((800, 600))
    screen.fill (colors["grey_light"])

    font.underline_adjustment = 0.5
    font.pad = True
    font.render_to(screen, (32, 32), "Hello World", colors["red"],
                   colors['grey_dark'], ptsize=64,
                   style=freetype.STYLE_UNDERLINE|freetype.STYLE_OBLIQUE)
    font.pad = False

    font.render_to(screen, (32, 128), "abcdefghijklm", colors["grey_dark"],
                   colors["green"], ptsize=64)

    font.vertical = True
    font.render_to(screen, (32, 200), "Vertical?", colors["blue"],
                   None, ptsize=32)
    font.vertical = False

    font.render_to(screen, (64, 190), "Let's spin!", colors["red"],
                   None, ptsize=48, rotation=55)

    font.render_to(screen, (160, 290), "All around!", colors["green"],
                   None, ptsize=48, rotation=-55)

    font.render_to(screen, (250, 220), "and BLEND",
                   pygame.Color(255, 0, 0, 128), None, ptsize=64)

    font.render_to(screen, (265, 237), "or BLAND!",
                   pygame.Color(0, 0xCC, 28, 128), None, ptsize=64)

    # Some pinwheels
    font.origin = True
    for angle in range(0, 360, 45):
        font.render_to(screen, (200, 500), ")", pygame.Color('black'),
                       ptsize=48, rotation=angle)
    font.vertical = True
    for angle in range(15, 375, 30):
        font.render_to(screen, (600, 400), "|^*", pygame.Color('orange'),
                       ptsize=48, rotation=angle)
    font.vertical = False
    font.origin = False

    utext = pygame.compat.as_unicode(r"I \u2665 Unicode")
    font.render_to(screen, (298, 320), utext, pygame.Color(0, 0xCC, 0xDD),
                   None, ptsize=64)

    utext = pygame.compat.as_unicode(r"\u2665")
    font.render_to(screen, (480, 32), utext, colors["grey_light"],
                   colors["red"], ptsize=148)

    font.render_to(screen, (380, 380), "...yes, this is an SDL surface",
                   pygame.Color(0, 0, 0),
                   None, ptsize=24, style=freetype.STYLE_STRONG)

    pygame.display.flip()

    while 1:
        if pygame.event.wait().type in (QUIT, KEYDOWN, MOUSEBUTTONDOWN):
            break

    pygame.quit()

if __name__ == "__main__":
    run ()
