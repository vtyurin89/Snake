import pygame as pg
from settings import Settings
import threading
from random import randint


class Snake:

    def __init__(self, screen):
        self.screen = screen
        self.settings = Settings()
        self.color = self.settings.snake_color

        self.snake_dir = (0, 0)
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

        #еда
        self.food_x = randint(0, 9) * 10
        self.food_y = randint(0, 9) * 10
        self.new_food_check = False
        self.rnd_pos = []

        #для временного тика
        self.event = threading.Event()

        #ректы змеи и еды
        self.snake_main = pg.rect.Rect(
            (self.settings.snake_x, self.settings.snake_y, self.settings.tile_W, self.settings.tile_H))
        self.rnd_pos = self.random_position()
        self.food = pg.rect.Rect(
            (self.rnd_pos, self.rnd_pos, self.settings.tile_W, self.settings.tile_H))
        self.snake_list = [self.snake_main.copy()]

    def random_position(self):
        self.rnd_pos = randint(0, self.settings.tile_num - 1) * self.settings.tile_W
        return self.rnd_pos

    def show_snake(self):
        [pg.draw.rect(self.screen, self.settings.snake_color, segment) for segment in self.snake_list]

        #движение
        self.event.wait(0.2)
        self.snake_main.move_ip(self.snake_dir)
        self.snake_list.append(self.snake_main.copy())
        self.snake_list = self.snake_list[1:]

        if self.move_right:
            self.snake_dir = (self.settings.tile_W, 0)
        elif self.move_left:
            self.snake_dir = (- self.settings.tile_W, 0)
        elif self.move_up:
            self.snake_dir = (0, - self.settings.tile_H)
        elif self.move_down:
            self.snake_dir = (0, self.settings.tile_H)

    def eat_food(self):
        pg.draw.rect(self.screen, self.settings.food_color, self.food)
        #поедание еды и генерация новой
        if pg.Rect.colliderect(self.food, self.snake_main):
            self.snake_list.append(self.snake_main.copy())
            print("Счёт: ", len(self.snake_list))

            self.new_food_check = True
            while self.new_food_check:
                self.rnd_pos = self.random_position()
                self.food = pg.rect.Rect((self.rnd_pos, self.rnd_pos, self.settings.tile_W, self.settings.tile_H))

                # нужен код проверки еды
                if pg.Rect.colliderect(self.food, self.snake_main):
                    self.food = pg.rect.Rect((self.rnd_pos, self.rnd_pos, self.settings.tile_W, self.settings.tile_H))
                else:
                    self.new_food_check = False







