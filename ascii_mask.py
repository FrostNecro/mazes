from mask import Mask
from masked_grid import MaskedGrid
from algoritms import *


def from_txt(file):
    with open(file) as f:
        lines = f.readlines()
        rows = len(lines)
        columns = len(lines[0]) - 1
        mask = Mask(rows, columns)

        for row in range(rows):
            for col in range(columns):
                if lines[row][col] == "X":
                    mask[[row, col]] = False
                else:
                    mask[[row, col]] = True
    return mask

maskew = from_txt("mask.txt")

grid = MaskedGrid(maskew)
HuntAndKill(grid).run()
print(grid.random_cell())

grid.to_png()
