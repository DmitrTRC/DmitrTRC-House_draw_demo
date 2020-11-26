import pygame


def main():
    screen_width = 800
    screen_height = 800
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
    draw_house(window, house_x, house_y, house_width, house_height)


def draw_background(window):
    earth_color = 'darkgreen'
    sky_color = 'deepskyblue3'
    pygame.draw.rect(window, earth_color, ((0, window.get_height() // 2),
                                           (window.get_width() - 1, window.get_height() - 1)))
    pygame.draw.rect(window, sky_color, ((0, 0), (window.get_width() - 1, window.get_height() // 2)))


def draw_house(window, x, y, width, height):
    foundation_height = height // 8
    walls_height = height // 2
    walls_width = 7 * width // 8
    roof_height = height - walls_height - foundation_height

    draw_foundation(window, x, y, width, foundation_height)
    draw_walls(window, x, y - walls_height, walls_width, walls_height)
    draw_roof(window, x, y - walls_height, width, roof_height)


def draw_foundation(window, x, y, width, height):
    foundation_color = 'peru'
    pygame.draw.rect(window, foundation_color, ((x - width // 2, y), (width, height)))


def draw_walls(window, x, y, width, height):
    walls_color = ' peachpuff'
    pygame.draw.rect(window, walls_color, ((x - width // 2, y), (width, height)))
    draw_house_window(window, x, y + height // 4, width // 3, height // 2)


def draw_house_window(window, x, y, width, height):
    window_color = 'cornflowerblue'
    window_border_color = 'khaki4'
    pygame.draw.rect(window, window_color, ((x - width // 2, y), (width, height)))
    pygame.draw.rect(window, window_border_color, ((x - width // 2, y), (width, height)), 10)
    pygame.draw.line(window, window_border_color, (x, y), (x, y + height), 3)
    pygame.draw.line(window, window_border_color,
                     (x - width // 2, y + height // 2), (x + width // 2, y + height // 2), 3)


def draw_roof(window, x, y, width, height):
    roof_color = 'sienna4'
    pygame.draw.polygon(window, roof_color, ((x - width // 2, y), (x + width // 2, y), (x, y - height)))


if __name__ == '__main__':
    main()
