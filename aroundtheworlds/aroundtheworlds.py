""" Two different worlds, only one controller.
"""

import pygame as pg


def main():
    print('Around the Worlds in 80 days.')

    going = True

    pg.display.init()
    pg.font.init()
    pg.display.set_caption("Around the Worlds in 80 days.")

    screen = pg.display.set_mode((640,480))
    clock = pg.time.Clock()

    left_screen = screen.subsurface((0, 0, 320, 480))
    right_screen = screen.subsurface((320, 0, 320, 480))

    left_screen.fill(pg.Color('blue'))
    right_screen.fill(pg.Color('red'))


    while going:
        events = pg.event.get()
        for e in events:
            if e.type == pg.QUIT or e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
                going = 0
            if e.type == pg.KEYDOWN:
                pass

        pg.display.flip()

        # limit the frame rate to 30fps.
        clock.tick(30)


if __name__ == '__main__':
    main()