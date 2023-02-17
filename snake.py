import pygame as pg
from settings import Settings
import threading
from random import randint


class Snake():

    def __init__(self, screen):
        self.screen = screen
        self.settings = Settings()
        self.color = self.settings.snake_color
        self.snake_length = 1

        self.snake_dir = (0, 0)
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

        #еда
        self.new_food_check = False

        #для временного тика
        self.event = threading.Event()

        #ректы змеи и еды
        self.snake_main = pg.rect.Rect(
            (0, 0, self.settings.tile_W - 2, self.settings.tile_H - 2))
        self.rnd_pos = self.random_position()
        self.snake_main.topleft = [self.rnd_pos, self.rnd_pos]
        self.food = pg.rect.Rect(
            (0, 0, self.settings.tile_W - 2, self.settings.tile_H - 2))
        self.food.topleft = [self.rnd_pos, self.rnd_pos]
        self.snake_list = [self.snake_main.copy()]

    def random_position(self):
        self.rnd_pos = randint(0, self.settings.tile_num - 1) * self.settings.tile_W + self.settings.snake_tile_border
        return self.rnd_pos

    def show_snake(self):
        [pg.draw.rect(self.screen, self.settings.snake_color, segment) for segment in self.snake_list]

        #движение
        self.event.wait(0.12)
        self.snake_main.move_ip(self.snake_dir)
        self.snake_list.append(self.snake_main.copy())
        self.snake_list = self.snake_list[-self.snake_length:]

        if self.move_right:
            self.snake_dir = (self.settings.tile_W, 0)
        elif self.move_left:
            self.snake_dir = (- self.settings.tile_W, 0)
        elif self.move_up:
            self.snake_dir = (0, - self.settings.tile_H)
        elif self.move_down:
            self.snake_dir = (0, self.settings.tile_H)

        #границы
        if self.snake_main.right > self.settings.width and self.move_right:
            self.snake_main.right = - self.settings.snake_tile_border
        if self.snake_main.left < 0 and self.move_left:
            self.snake_main.left = self.settings.width + self.settings.snake_tile_border
        if self.snake_main.bottom > self.settings.height and self.move_down:
            self.snake_main.bottom = -self.settings.snake_tile_border
        if self.snake_main.top < 0 and self.move_up:
            self.snake_main.top = self.settings.height + self.settings.snake_tile_border



    #возможная переделка движения? (сейчас не используется)
    def show_snake_alt(self):
        [pg.draw.rect(self.screen, self.settings.snake_color, segment) for segment in self.snake_list]

        #движение
        self.event.wait(0.12)
        self.snake_main.move_ip(self.snake_dir)
        self.snake_list.append(self.snake_main.copy())
        self.snake_list = self.snake_list[-self.snake_length:]

        if self.move_right:
            self.snake_dir = (self.settings.tile_W, 0)
        elif self.move_left:
            self.snake_dir = (- self.settings.tile_W, 0)
        elif self.move_up:
            self.snake_dir = (0, - self.settings.tile_H)
        elif self.move_down:
            self.snake_dir = (0, self.settings.tile_H)

        #границы
        if self.snake_main.right > self.settings.width and self.move_right:
            self.snake_main.right = - self.settings.snake_tile_border
        if self.snake_main.left < 0 and self.move_left:
            self.snake_main.left = self.settings.width + self.settings.snake_tile_border
        if self.snake_main.bottom > self.settings.height and self.move_down:
            self.snake_main.bottom = -self.settings.snake_tile_border
        if self.snake_main.top < 0 and self.move_up:
            self.snake_main.top = self.settings.height + self.settings.snake_tile_border



    def eat_food(self):
        pg.draw.rect(self.screen, self.settings.food_color, self.food)

        #поедание еды и генерация новой
        if pg.Rect.colliderect(self.food, self.snake_main):
            self.snake_list.append(self.snake_main.copy())
            self.snake_length = self.snake_length + 1
            print("Счёт: ", len(self.snake_list))

            self.new_food_check = True
            while self.new_food_check:
                self.rnd_food_x = self.random_position()
                self.rnd_food_y = self.random_position()
                if not any([self.segment.collidepoint(self.rnd_food_x, self.rnd_food_y) for self.segment in self.snake_list]):
                    self.food = pg.rect.Rect((self.rnd_food_x, self.rnd_food_y, self.settings.tile_W - 2, self.settings.tile_H - 2))
                    self.new_food_check = False

    def snake_lose(self):
        self.collide_check = pg.Rect.collidelist(self.snake_main, self.snake_list[1:])
        self.snake_hit = False
        if self.collide_check < len(self.snake_list)-3 and self.collide_check != -1 and self.collide_check != 0:
            print(self.collide_check)
            self.snake_hit = True




