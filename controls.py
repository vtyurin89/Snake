import sys
import pygame as pg



def events(snake):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            #вниз
            if event.key == pg.K_s and not snake.move_up:
                snake.move_right = False
                snake.move_left = False
                snake.move_up = False
                snake.move_down = True
            #вправо
            if event.key == pg.K_d and not snake.move_left:
                snake.move_right = True
                snake.move_left = False
                snake.move_up = False
                snake.move_down = False
            #влево
            if event.key == pg.K_a and not snake.move_right:
                snake.move_right = False
                snake.move_left = True
                snake.move_up = False
                snake.move_down = False
            #вверх
            if event.key == pg.K_w and not snake.move_down:
                snake.move_right = False
                snake.move_left = False
                snake.move_up = True
                snake.move_down = False

