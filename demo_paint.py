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
        draw_image(screen)
        pygame.display.flip()
    pygame.quit()


def draw_image(window):
    house_x = window.get_width() // 2
    house_y = window.get_height() // 2 * 3
    house_width = window.get_width() // 3
    house_height = house_width * 4 / 3

    draw_background()
    draw_house()


def draw_background():
    pass


def draw_house():
    pass


if __name__ == '__main__':
    main()
