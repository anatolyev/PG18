# Example file showing a circle moving on screen
import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def render(self, screen):
        for x in range(self.width):
            for y in range(self.height):
                pygame.draw.rect(screen,
                                 pygame.Color("white"),
                                 (x * self.cell_size + self.left,
                                  y * self.cell_size + self.top,
                                  self.cell_size,
                                  self.cell_size),
                                 1)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

# pygame setup
def main():
    pygame.init()
    size = width, height = 600, 400
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    board = Board(18, 12)
    board.set_view(100, 100, 15)
    running = True
    v = 500
    dt = 0
    # limits FPS to 60
    fps = 30

    while running:
        # fill the screen with a color to wipe away anything from last frame

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        board.render(screen)
        # flip() the display to put your work on screen
        pygame.display.flip()

        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(fps) / 1000

    pygame.quit()


if __name__ == '__main__':
    main()