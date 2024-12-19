import os
import sys
import pygame


def main():
    # pygame setup
    pygame.init()
    size = width, height = (1280, 720)
    screen = pygame.display.set_mode(size)
    screen.fill("purple")
    clock = pygame.time.Clock()
    image = load_image('bomb.png')
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.blit(image, event.pos)
        # RENDER YOUR GAME HERE

        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60
    pygame.quit()

def load_image(name):
    fullname = os.path.join('images', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением {fullname} не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    return image

if __name__ == '__main__':
    main()