# Общие зависимости:
import os
import sys
import pygame

# Внутренние зависимости:
from data.config import *
from data.classes import *


def load_image(name, color_key=None):
    """Загрузка изображений"""
    fullname = os.path.join(IMAGES, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Невозможно загрузить изображение из файла:', fullname)
        raise SystemExit(message)
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def terminate():
    """Выход из игры"""
    pygame.quit()
    sys.exit()

def game_cycle():
    """Главный игровой цикл"""
    dragon = AnimatedSprite(load_image("dragon_sheet8x2.png"), 8, 2, 100, 100)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        screen.fill(pygame.Color(0, 0, 0))

        all_sprites.draw(screen)
        all_sprites.update()

        pygame.display.flip()
        clock.tick(FPS)
    terminate()

