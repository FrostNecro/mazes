from grid import Grid
from cell import Cell

class MaskedGrid(Grid):
    """description of class"""
    def __init__(self, mask):
        self.mask = mask
        super().__init__(self.mask.rows, self.mask.columns)

    def prepare_grid(self):
        for row in range(self.rows):
            columnList = {}
            for column in range(self.columns):
                if self.mask[[row, column]]:
                    cell = Cell(row, column)
                    columnList.update({column: cell})
                else:
                    columnList.update({column: None})
            self.cellsList.update({row: columnList})
        return self.cellsList

    def random_cell(self):
        row, col = self.mask.random_location()
        return self.cellsList[row][col]

    def size(self):
        return self.mask.count()


