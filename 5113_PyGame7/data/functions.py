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


def generate_level(level):
    """ Отрисовка уровня """

    # Словарь с изображениями клеточек игрового поля:
    tile_images = {
        'wall': load_image('box.png'),
        'empty': load_image('grass.png'),
        'player': load_image('mar.png'),
    }

    for y in range(len(level)):
        for x in range(len(level[y])):
            match level[y][x]:
                case '.': Tile(tile_images, 'empty', x, y)
                case '#': Tile(tile_images, 'wall', x, y)
                case "@": Tile(tile_images, 'player', x, y)

    return None


def terminate():
    """Выход из игры"""
    pygame.quit()
    sys.exit()


def rules_screen():
    rules_text = ["Правила игры",
                  "",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно!",
                  "А иначе они просто не влезут на экран с игрой"]
    background_image = pygame.transform.scale(load_image('fon.jpg'), SIZE)
    screen.blit(background_image, (0, 0))  # Выводим фон
    text_coord = 60
    for line in rules_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        rules_rect = string_rendered.get_rect()
        print("1 intro_rect=", *rules_rect)
        rules_rect.top = text_coord  # Записываем новые координаты у
        rules_rect.x = 10  # Отступ текста от левого края
        print("2 intro_rect=", *rules_rect)
        print()
        screen.blit(string_rendered, rules_rect)
        text_coord += rules_rect.height + 10  # Переводим строку текста

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type in (pygame.KEYUP, pygame.MOUSEBUTTONUP):
                game_cycle("Марио", 0)
        pygame.display.flip()
        clock.tick(FPS)


def load_level(filename):
    filename = LEVELS + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))
    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))



def game_cycle(user_name, difficulty):
    """Главный игровой цикл"""

    generate_level(load_level(LEVELS_LIST[difficulty]))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        screen.fill(pygame.Color(0, 0, 0))
        tiles_group.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)
    terminate()

