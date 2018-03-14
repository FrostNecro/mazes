from grid import Grid

class DistanceGrid(Grid):

    def contents_of(self, cell):
        try:
            if self.distances.cells and (self.distances.cells[cell] + 1):
                return str(hex(self.distances.cells[cell]))[-1]
            else:
                return super().contents_of(cell)
        except KeyError:
            return super().contents_of(cell)
