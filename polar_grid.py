from grid import Grid

class PolarGrid(Grid):

    def to_png(self, cell_size=10, mode='backgrounds'):
        img_size = 2 * self.rows * cell_size
