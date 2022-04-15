from queue import Queue


class Object:
    def __init__(self, smell_diff=0, smell_value=0):
        self.smell_diff = smell_diff
        self.smell_value = smell_value

    def play(self, cells):
        return None

    def give_smell_around(self, map, filled_cells, start_cell, smell_value):
        q = Queue()
        q.put(start_cell)
        while not q.empty():
            cur_cell = q.get()
            cur_smell_value = cur_cell.smells[type(self)] - self.smell_diff
            if cur_smell_value <= 0:
                return None
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if 0 <= cur_cell.x + i <= map.width and 0 <= cur_cell.y + j <= map.height:
                        next_cell = map.cells[cur_cell.x + i][cur_cell.y + j]
                        if next_cell is not cur_cell:
                            if next_cell not in filled_cells:
                                next_cell.set_smell(cur_smell_value, type(self))
                                filled_cells.append(next_cell)
                                q.put(next_cell)

    def start_smell(self, map, start_cell):
        start_cell.set_smell(self.smell_value, type(self))
        self.give_smell_around(map, [start_cell], start_cell, self.smell_value - self.smell_diff)
