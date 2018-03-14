from mask import *
import masked_grid
import algoritms
from grid import *

mask = Mask(5, 5)

mask[[0, 0]] = False
mask[[2, 2]] = False
mask[[4, 4]] = False

grid = masked_grid.MaskedGrid(mask)
Tree = algoritms.RecursiveBacktracker(grid).run()
print(grid)

