import pygame


def main():
    screen_width = 1800
    screen_height = 1000
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_image()
        pygame.display.flip()
    pygame.quit()


def draw_image():
    pass


if __name__ == '__main__':
    main()
