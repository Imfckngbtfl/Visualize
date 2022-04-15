import pygame


def Draw_Cell(main_sf: pygame.Surface, cells, width, length, map):

    for i in cells:
        for j in i:
            sf_сell = pygame.Surface((width, length))
            sf_сell.fill(j.color)
            rect = sf_сell.get_rect(center=(map[j.y][j.y].x, map[j.x][j.y].y))
            main_sf.blit(sf_сell, rect)



