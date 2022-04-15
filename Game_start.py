import pygame
import numpy as np
from Creature_graphics import Creature
import Map_graphics
from Cell_graphics import Draw_Cell
w = 200
h = 200
pygame.init()


CONST_OF_SIZE_OF_SQUARE = 5
WHITE = (255, 255, 255)
game = True
FPS = 60
screen = pygame.display.set_mode((1920, 1080))
screen.fill((255,255,255))
clock = pygame.time.Clock()

Map = Map_graphics.Map(w+1, h+1, CONST_OF_SIZE_OF_SQUARE, 1)

main_map = Map.create_map()
#Map.print_info_points()
screen.blit(main_map, (0, 0))
#Map.print_info_points()
#creature1 = Creature(349.0, 390.0, CONST_OF_SIZE_OF_SQUARE, CONST_OF_SIZE_OF_SQUARE, (255, 0, 0))

#test_l = [(2, 0), (3, 5)]# test list


def start_graphics(cells):
    while game:
        #clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                pygame.quit()
            '''
            if event.type == pygame.MOUSEMOTION:
                print("Позиция :", event.pos)
            '''
        #print(Map.arr)
        #main_map = Map.create_map()  # заполнение карты
        Draw_Cell(main_map, cells, 40, 40, Map.arr)
        ##screen.fill((0, 0, 0))  # заполнение экрана
        #main_map.blit(creature1.image, creature1.rect)  # заполнение карты
        screen.blit(main_map, (0, 0))  # заполнение экрана
        pygame.display.update()  # flip экрана



       # creature1.update_top(390.0, 349.0)  # изменение координат
        pygame.display.update()