# Example file showing a basic pygame "game loop"
import pygame


def main():
    # pygame setup
    pygame.init()
    size = width, height = (1280, 720)
    screen = pygame.display.set_mode(size)
    screen.fill("purple")
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # RENDER YOUR GAME HERE

        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60
    pygame.quit()

if __name__ == '__main__':
    main()