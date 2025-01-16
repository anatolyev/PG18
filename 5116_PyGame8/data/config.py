import pygame
from pygame.locals import RESIZABLE

# Константы:
GAME_NAME = "Марио"
FPS = 50
SIZE = WIDTH, HEIGHT = 400, 300
STEP = 50
IMAGES = "images/"
SOUNDS = "sounds/"

# Конфигурации PyGame:
pygame.init()

# Игровое поле
tile_width = tile_height = 50

# Шрифт
font = pygame.font.Font(None, 30)

# Задержка для зажатой клавиши. Например, при движении игрока.
pygame.key.set_repeat(200, 70)

screen = pygame.display.set_mode(SIZE, RESIZABLE)
clock = pygame.time.Clock()

# Группы спрайтов
all_sprites = pygame.sprite.Group()
