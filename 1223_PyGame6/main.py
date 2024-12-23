import os
import sys
import pygame
from random import randrange, randint

ALL_SPRITES = pygame.sprite.Group()


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(ALL_SPRITES)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        while 1:
            self.vx = randint(-5, 5)
            self.vy = randrange(-5, 5)
            if self.vx and self.vy:
                break

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)


def main():
    # pygame setup
    pygame.init()
    size = width, height = (1280, 720)
    screen = pygame.display.set_mode(size)

    for _ in range(10):
        Ball(20, 400, 400)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                ALL_SPRITES.update(event)
        screen.fill("purple")
        # RENDER YOUR GAME HERE
        ALL_SPRITES.draw(screen)
        ALL_SPRITES.update()
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60
    pygame.quit()

def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением {fullname} не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()  # создаёт новую копию изображения с таким же форматом пикселей, как у экрана
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()  # метод для преобразования изображения с сохранением информации о прозрачности
    return image

if __name__ == '__main__':
    main()