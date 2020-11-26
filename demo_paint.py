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
    house_y = window.get_height() // 5 * 3
    house_width = window.get_width() // 3
    house_height = house_width * 4 / 3

    draw_background(window)
    draw_house(window)


def draw_background(window):
    earth_color = 'darkgreen'
    sky_color = 'deepskyblue3'
    pygame.draw.rect(window, earth_color, ((0, window.get_height() // 2),
                                           (window.get_width() - 1, window.get_height() - 1)))
    pygame.draw.rect(window, sky_color, ((0, 0), (window.get_width() - 1, window.get_height() // 2)))


def draw_house(window):
    draw_foundation(window)
    draw_walls(window)
    draw_roof(window)


def draw_foundation(window):
    pass


def draw_walls(window):
    pass


def draw_roof(window):
    pass


if __name__ == '__main__':
    main()
