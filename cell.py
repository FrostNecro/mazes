from distances import Distances

class Cell:
    north = None
    south = None
    east = None
    west = None

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.links = {}
        self.unvisited = True
        self.step = 0


    def link(self, cell, bidi=True):
        self.links[cell] = True
        if bidi:
            cell.link(self, False)

    def unlink(self, cell, bidi=True):
        self.links.pop(cell)
        if bidi:
            cell.unlink(self, False)

    def links_list(self):
        return self.links.keys()

    def isLinked(self, cell):
        return bool(self.links.get(cell))

    def neighbors(self):
        sides = [self.north, self.south, self.east, self.west]
        neighborsList = []
        for side in sides:
            if side is not None:
                neighborsList.append(side)
        return neighborsList
    def distances(self):
        distances = Distances(self)
        frontier = [self]

        while any(frontier):
            new_frontier = []

            for cell in frontier:
                for linked in cell.links_list():
                    if not linked in distances.getCells():
                        distances.cells[linked] = distances.cells[cell] + 1
                        new_frontier.append(linked)
            frontier = new_frontier

        return distances
