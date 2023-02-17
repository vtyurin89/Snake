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
        game_over = snake.snake_hit

        if game_over:
            snake.snake_dir = (0, 0)
            snake.move_right = False
            snake.move_left = False
            snake.move_up = False
            snake.move_down = False
            final_message = settings.final_font.render(settings.final_message, True, (180, 0, 0))
            message_rect = final_message.get_rect()
            message_rect_position = [settings.middle_pos_W - message_rect.width / 2, settings.middle_pos_H - message_rect.height / 2]
            screen.blit(final_message, message_rect_position)
        pg.display.flip()



if __name__ == "__main__":
    run_game()


