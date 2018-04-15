""" Two different worlds, only one controller.
"""

import pygame as pg


class Baloon(pg.sprite.DirtySprite):
    def __init__(self):
        pg.sprite.DirtySprite.__init__(self)
        self.image = pg.Surface((20, 20))
        self.image.fill(pg.Color('green'))
        self.rect = self.image.get_rect()

    def update(self):
        self.dirty = 1


def main():
    print('Around the Worlds in 80 days.')

    going = True

    pg.display.init()
    pg.font.init()
    pg.display.set_caption("Around the Worlds in 80 days.")

    clock = pg.time.Clock()

    screen = pg.display.set_mode((640,480))
    left_screen = screen.subsurface((0, 0, 320, 480))
    right_screen = screen.subsurface((320, 0, 320, 480))

    left_balloon = Baloon()
    right_balloon = Baloon()
    left_sprites = pg.sprite.LayeredDirty([left_balloon])
    right_sprites = pg.sprite.LayeredDirty([right_balloon])

    left_background = left_screen.copy()
    right_background = right_screen.copy()
    left_background.fill(pg.Color('blue'))
    right_background.fill(pg.Color('red'))

    left_sprites.clear(left_screen, left_background)
    right_sprites.clear(left_screen, right_background)


    while going:
        events = pg.event.get()
        for e in events:
            if e.type == pg.QUIT or e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
                going = 0
            if e.type == pg.KEYDOWN:
                pass

        left_sprites.update()
        right_sprites.update()

        left_rects = left_sprites.draw(left_screen)
        right_rects = right_sprites.draw(right_screen)
        pg.display.update(left_rects + right_rects)

        clock.tick(30)


if __name__ == '__main__':
    main()