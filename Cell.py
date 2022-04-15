from Berry import Berry
from Creature import Creature
from Apple import Apple

def clamp(min_value, value, max_value):
    if value < min_value:
        return min_value
    if value > max_value:
        return max_value
    return value


class Cell:
    def __init__(self, objects, x, y):
        self.objects = objects
        self.smells = {Berry : 0, Apple : 0, Creature : 0}
        self.default_smell_colors = {Berry : [255, 0, 0], Apple: [0, 255, 0], Creature: [0, 0, 255]}
        self.x = x
        self.y = y
        self.color = (255, 255, 255)

    def set_object(self, object):
        self.objects.append(object)

    def set_smell(self, smell_value, type):
        self.smells[type] = clamp(0, self.smells[type] + smell_value, 100)
        cur_color = [0, 0, 0]
        for i in self.smells:
            for j in range(3):
                cur_color[j] += int(self.default_smell_colors[i][j]*self.smells[i]*0.01)
                cur_color[j] = clamp(0, cur_color[j], 255)
        self.color = tuple(cur_color)


    def update(self):
        return None
    def delete_smell(self, smell_value, type):
        self.smells[type] = clamp(0, self.smells[type] - smell_value, 100)
        self.color = (self.smells[Berry], self.smells[Apple], self.smells[Creature])

    def remove_object(self, object):
        self.objects.pop(object)
