import gc
import time
import algoritms
from colored_grid import ColoredGrid
from distance_grid import DistanceGrid

startTime = time.time()
grid = ColoredGrid(10, 10)

Tree = algoritms.RecursiveBacktracker(grid).run()
print(grid)
finishTime = time.time()
totalTime = finishTime - startTime
print(totalTime)

gc.collect()
