from Map import Map
from Creature import Creature
from Berry import Berry
from Apple import Apple
from Game_start import start_graphics
import random
w = 200
h = 200
if __name__ == '__main__':
    m = Map(w, h)
    m.generate()
    c = Creature()
    b = Berry()
    a = Apple()
    #m.set_cell(3, 2, b)
    #m.set_cell(7, 8, a)
    #m.set_cell(5, 5, c)
    for i in m.cells:
        for j in i:
            k = random.randint(0, 100)
            if k <= 0:
                l = random.randint(0, 2)
                if l == 0:
                    c = Creature()
                    m.set_cell(j.x, j.y, c)
                if l == 1:
                    b = Berry()
                    m.set_cell(j.x, j.y, b)
                if l == 2:
                    a = Apple()
                    m.set_cell(j.x, j.y, a)
    start_graphics(m.cells)


