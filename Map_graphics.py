import pygame
import numpy as np


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def pprint(self):
        print((self.x, self.y))


class Map:
    def __init__(self, width_of_list: int, length_of_list: int, SIDE_OF_BOX: float, LINE_CHIKNESS: float):
        self.arr = None
        self.width_of_list = width_of_list
        self.length_of_list = length_of_list
        self.SIDE_OF_BOX = SIDE_OF_BOX
        self.LINE_CHIKNESS = LINE_CHIKNESS

    def create_map(self) -> pygame.Surface:
        W = (self.width_of_list + 1) * self.LINE_CHIKNESS + self.SIDE_OF_BOX * self.width_of_list
        H = (self.length_of_list + 1) * self.LINE_CHIKNESS + self.SIDE_OF_BOX * self.length_of_list
        map = pygame.Surface((W, H))
        x = 0
        y = 0
        for i in range(self.width_of_list + 1):
            pygame.draw.line(map, (255, 255, 255), (x, y), (x, H))
            x += self.SIDE_OF_BOX + self.LINE_CHIKNESS

        x2 = 0
        y2 = 0
        for i in range(self.length_of_list + 1):
            pygame.draw.line(map, (255, 255, 255), (x2, y2), (W, y2))
            y2 += self.SIDE_OF_BOX + self.LINE_CHIKNESS

        l = []
        k = 1
        for i in range(self.length_of_list):
            p = 1
            l2 = []
            for j in range(self.width_of_list):
                if k == 1 and p == 1:
                    l2 += [Point(self.SIDE_OF_BOX / 2 + self.LINE_CHIKNESS, self.SIDE_OF_BOX / 2 + self.LINE_CHIKNESS)]
                elif k == 1 and p != 1:
                    l2 += [
                        Point(p * self.SIDE_OF_BOX - 0.5 * self.SIDE_OF_BOX + p * self.LINE_CHIKNESS,
                              self.SIDE_OF_BOX / 2 + self.LINE_CHIKNESS)]
                elif p == 1 and k != 1:
                    l2 += [
                        Point(self.SIDE_OF_BOX / 2 + self.LINE_CHIKNESS,
                              k * self.SIDE_OF_BOX - 0.5 * self.SIDE_OF_BOX + k * self.LINE_CHIKNESS)]
                elif k != 1 and p != 1:
                    l2 += [Point(p * self.SIDE_OF_BOX - 0.5 * self.SIDE_OF_BOX + p * self.LINE_CHIKNESS,
                                 k * self.SIDE_OF_BOX - 0.5 * self.SIDE_OF_BOX + k * self.LINE_CHIKNESS)]
                p += 1
            l += l2
            l2 = []
            k += 1
        self.arr = np.array(l).reshape(self.length_of_list, self.width_of_list)
        return map

    def print_info_points(self):
        for i in self.arr:
            for j in i:
                j.pprint()

