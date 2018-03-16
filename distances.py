class Distances:
    def __init__(self, root):
        self.root = root
        self.cells = {}
        self.cells[self.root] = 0

    def getCells(self):
        return self.cells.keys()

    def path_to(self, goal):
        current = goal
        breadcrumbs = Distances(self.root)
        breadcrumbs.cells[current] = self.cells[current]

        while not current == self.root:
            for neighbor in current.links_list():
                if self.cells[neighbor] < self.cells[current]:
                    breadcrumbs.cells[neighbor] = self.cells[neighbor]
                    current = neighbor
                    break

        return breadcrumbs

    def maxim(self):
        max_distance = 0
        max_cell = self.root

        for cell in self.cells:
            distance = self.cells[cell]
            if distance > max_distance:
                max_cell = cell
                max_distance = distance

        return max_cell, max_distance
