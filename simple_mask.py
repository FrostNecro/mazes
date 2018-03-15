from mask import *
import masked_grid
import algoritms
from grid import *

mask = Mask(10, 10)

mask[[0, 0]] = False
mask[[0, 1]] = False
mask[[0, 2]] = False

grid = masked_grid.MaskedGrid(mask)
Tree = algoritms.RecursiveBacktracker(grid).run()
print(grid)

