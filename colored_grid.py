import grid

class ColoredGrid(grid.Grid):

    def getDistances(self, distances):
        self.distances = distances
        self.maximum = self.distances.maxim()[1]

    def background_color_for(self, cell):
        try:
            if self.distances.cells[cell]:
                distance = self.distances.cells[cell]
            else:
                return None
        except KeyError:
            return None
        intensity = float((self.maximum - distance))/self.maximum
        dark = int(255 * intensity)
        bright = int(128 + (127 * intensity))
        color = (dark, dark, bright)
        return color
                     