from Cell import Cell


class Map:

    def __init__(self, w, h):
        self.cells = []
        self.width = w
        self.height = h

    def generate(self):
        for i in range(self.height + 1):
            cell_row = []
            for j in range(self.width + 1):
                k = Cell([], i, j)
                cell_row.append(k)
            self.cells.append(cell_row)

    def set_cell(self, x, y, object):
        self.cells[x][y].set_object(object)
        object.start_smell(self, self.cells[x][y])