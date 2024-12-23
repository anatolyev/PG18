import os
import sys
import pygame
from random import randrange, randint

pygame.init()
size = width, height = (789, 600)
screen = pygame.display.set_mode(size)
ALL_SPRITES = pygame.sprite.Group()
HORIZONTAL_BORDERS = pygame.sprite.Group()
VERTICAL_BORDERS = pygame.sprite.Group()


def main():
    # pygame setup


    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                Landing(event.pos)
                # ALL_SPRITES.update(event)
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
    print('Изображение загружено!')
    if colorkey is not None:
        image = image.convert()  # создаёт новую копию изображения с таким же форматом пикселей, как у экрана
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()  # метод для преобразования изображения с сохранением информации о прозрачности
    print('Изображение вернул!')
    return image



class Mountain(pygame.sprite.Sprite):
    image = load_image("mountains.png")

    def __init__(self, size):
        super().__init__(ALL_SPRITES)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        # располагаем горы внизу
        self.rect.bottom = size[1]




class Landing(pygame.sprite.Sprite):
    image = load_image("pt.png")

    def __init__(self, pos):
        super().__init__(ALL_SPRITES)
        self.image = Landing.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if not pygame.sprite.collide_mask(self, mountain):
            self.rect = self.rect.move(0, 1)


if __name__ == '__main__':
    mountain = Mountain(size)
    main()