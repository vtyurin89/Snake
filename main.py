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
        snake.snake_lose()
        pg.display.flip()
        snake.snake_lose()
        game_over = snake.snake_moose
        if game_over:
            print("GAME OVER")
            snake.snake_dir = (0, 0)
            snake.move_right = False
            snake.move_left = False
            snake.move_up = False
            snake.move_down = False
            break



if __name__ == "__main__":
    run_game()


