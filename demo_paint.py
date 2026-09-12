import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS = 60

HALF = 2
THIRD = 3
FOURTH = 4
FIFTH = 5
SEVENTH_EIGHTHS_NUMERATOR = 7
EIGHTH = 8

WINDOW_BORDER_WIDTH = 10
WINDOW_LINE_WIDTH = 3

EARTH_COLOR = 'darkgreen'
SKY_COLOR = 'deepskyblue3'
FOUNDATION_COLOR = 'peru'
WALLS_COLOR = 'peachpuff'
HOUSE_WINDOW_COLOR = 'cornflowerblue'
WINDOW_BORDER_COLOR = 'khaki4'
ROOF_COLOR = 'sienna4'


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_image(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


def draw_image(window):
    window_width = window.get_width()
    window_height = window.get_height()
    house_x = window_width // HALF
    house_y = window_height // FIFTH * THIRD
    house_width = window_width // THIRD
    house_height = house_width * FOURTH / THIRD

    draw_background(window)
    draw_house(window, house_x, house_y, house_width, house_height)


def draw_background(window):
    window_width = window.get_width()
    window_height = window.get_height()
    pygame.draw.rect(window, EARTH_COLOR, (0, window_height // HALF,
                                           window_width, window_height // HALF))
    pygame.draw.rect(window, SKY_COLOR, (0, 0, window_width, window_height // HALF))


def draw_house(window, x, y, width, height):
    foundation_height = height // EIGHTH
    walls_height = height // HALF
    walls_width = SEVENTH_EIGHTHS_NUMERATOR * width // EIGHTH
    roof_height = height - walls_height - foundation_height

    draw_foundation(window, x, y, width, foundation_height)
    draw_walls(window, x, y - walls_height, walls_width, walls_height)
    draw_roof(window, x, y - walls_height, width, roof_height)


def draw_foundation(window, x, y, width, height):
    pygame.draw.rect(window, FOUNDATION_COLOR, ((x - width // HALF, y), (width, height)))


def draw_walls(window, x, y, width, height):
    pygame.draw.rect(window, WALLS_COLOR, ((x - width // HALF, y), (width, height)))
    draw_house_window(window, x, y + height // FOURTH, width // THIRD, height // HALF)


def draw_house_window(window, x, y, width, height):
    pygame.draw.rect(window, HOUSE_WINDOW_COLOR, ((x - width // HALF, y), (width, height)))
    pygame.draw.rect(window, WINDOW_BORDER_COLOR, ((x - width // HALF, y), (width, height)),
                     WINDOW_BORDER_WIDTH)
    pygame.draw.line(window, WINDOW_BORDER_COLOR, (x, y), (x, y + height), WINDOW_LINE_WIDTH)
    pygame.draw.line(window, WINDOW_BORDER_COLOR,
                     (x - width // HALF, y + height // HALF), (x + width // HALF, y + height // HALF),
                     WINDOW_LINE_WIDTH)


def draw_roof(window, x, y, width, height):
    pygame.draw.polygon(window, ROOF_COLOR,
                        ((x - width // HALF, y), (x + width // HALF, y), (x, y - height)))


if __name__ == '__main__':
    main()
