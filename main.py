import controls
import pygame as pg
from settings import Settings
from snake import Snake


def run_game():
    pg.init()
    settings = Settings()

    screen = pg.display.set_mode((settings.width, settings.height))
    pg.display.set_caption(settings.caption)
    clock = pg.time.Clock()
    snake = Snake(screen)

    while True:
        controls.events(snake)
        clock.tick(settings.fps)
        screen.fill(settings.bg_color)

        snake.show_snake()
        snake.eat_food()
        pg.display.flip()


if __name__ == "__main__":
    run_game()


