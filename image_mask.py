from mask import Mask
from masked_grid import MaskedGrid
from algoritms import *
from PIL import Image

def from_png(file):
    image = Image.open(file)
    mask = Mask(image.height, image.width)

    for row in range(mask.rows):
        for col in range(mask.columns):
             if image.getpixel((col,row)) == (0, 0, 0, 255):
                mask[[row, col]] = False
             else:
                mask[[row, col]] = True
    return mask

maskew = from_png("mask.png")

grid = MaskedGrid(maskew)
RecursiveBacktracker(grid).run()
start = grid[[19, 7]]
distances = start.distances()
grid.getDistances(distances)
grid.to_geosjson()
