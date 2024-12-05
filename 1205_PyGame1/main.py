# Документация:
# python - m pygame.docs

# Example file showing a basic pygame "game loop"
import pygame


def  draw1(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Hello, PyGame!", True, (100, 255, 100))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0),
                     (text_x - 10, text_y - 10,
                      text_w + 20, text_h + 20),
                     1)



if __name__ == '__main__':
    # pygame setup
    pygame.init()
    size = width, height = (800, 600)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        # screen.fill((0, 0, 0))

        # RENDER YOUR GAME HERE
        draw1(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(30)  # limits FPS to 30

    pygame.quit()