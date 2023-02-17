import pygame as pg


class Settings:

    def __init__(self):
        self.tile_W = 30
        self.tile_H = 30
        self.tile_num = 20

        #основное поле
        self.height = self.tile_H * self.tile_num
        self.width = self.tile_W * self.tile_num
        self.caption = "Snake"
        self.bg_color = (63, 107, 193)
        self.fps = 60
        self.middle_pos_H = self.height / 2
        self.middle_pos_W = self.width / 2

        #игровое поле
        self.grid_color = (43, 65, 114)
        self.grid_H = self.tile_H * self.tile_num
        self.grid_W = self.tile_W * self.tile_num
        self.blue = (43, 51, 70)
        self.border_color = (72, 67, 95)


        #змейка
        self.snake_color = (127, 255, 128)
        self.snake_tile_border = 1


        #еда
        self.food_color = 'red'

        #конец игры
        self.final_message = "GAME OVER"
        self.final_font = pg.font.Font(None, 36)

