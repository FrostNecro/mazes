
"""Algoritms for Creating Mazes"""

import random

class AldousBroeder:
    """This class takes grid as input and in 'run' it does all the work"""

    def __init__(self, grid):
        self.grid = grid

    def run(self):
        """First, it takes random cell, and it will iterate over random cells while unvisited > 0"""
        cell = self.grid.random_cell()
        unvisited = self.grid.size() - 1
        while unvisited > 0:
            neighbor = random.choice(cell.neighbors())

            if list(neighbor.links_list()) == []:
                cell.link(neighbor)
                unvisited -= 1

            cell = neighbor

        return self.grid

class BinaryTree:
    """This class takes grid as input and in 'run' it does all the work"""
    def __init__(self, grid):
        self.grid = grid
    def run(self):
        """It will iterate over cell by rows, starting at southwest corner, randomly connect north or east neighbor"""
        for cell in self.grid.each_cell():
            neighbors = []
            if cell.north:
                neighbors.append(cell.north)
            if cell.east:
                neighbors.append(cell.east)
            if neighbors:
                neighbor = random.choice(neighbors)
            if neighbor:
                cell.link(neighbor)
        return self.grid

class HuntAndKill:
    """Hunt and Kill allows to create maze with long curve passages"""

    def __init__(self, grid):
        self.grid = grid

    def run(self):
        current = self.grid.random_cell()

        while current:
            unvisited_neighbors = []

            for neighbor in current.neighbors():
                if neighbor.unvisited:
                    unvisited_neighbors.append(neighbor)

            if any(unvisited_neighbors):
                neighbor = random.choice(unvisited_neighbors)
                current.link(neighbor)
                current.unvisited = False
                current = neighbor
                current.unvisited = False
            else:
                current = False

                for cell in self.grid.each_cell():
                    visited_neighbors = []
                    for neighbor in cell.neighbors():
                        if not neighbor.unvisited:
                            visited_neighbors.append(neighbor)

                    if cell.unvisited and any(visited_neighbors):
                        current = cell
                        neighbor = random.choice(visited_neighbors)
                        current.link(neighbor)
                        current.unvisited = False
                        break

        return self.grid

class RecursiveBacktracker:
    """Implementation of Recursive Backtracker maze algoritm"""
    def __init__(self, grid):
        self.grid = grid
        self.start = grid.random_cell()
        self.start.unvisited = False

    def run(self):
        stack = []
        stack.append(self.start)

        while any(stack):
            current = stack[-1]
            neighbors = []
            for neighbor in current.neighbors():
                if neighbor.unvisited:
                    neighbors.append(neighbor)

            if neighbors == []:
                stack.pop()
            else:
                neighbor = random.choice(neighbors)
                current.link(neighbor)
                stack.append(neighbor)
                neighbor.unvisited = False

        return self.grid

class Sidewinder:
    """Impleventation of Sidewinder"""
    def __init__(self, grid):
        self.grid = grid

    def run(self):
        for row in self.grid.each_row():
            run = []

            for cell in row:
                run.append(cell)
                at_eastern_boundary = (cell.east is None)
                at_northern_boundary = (cell.north is None)
                should_close_out = at_eastern_boundary or (not at_northern_boundary and random.randint(0, 1) == 0)
                if should_close_out:
                    member = random.choice(run)
                    if member.north:
                        member.link(member.north)
                    run = []
                else:
                    cell.link(cell.east)
        return self.grid

class Wilsons:
    def __init__(self, grid):
        self.grid = grid

    def run(self):
        unvisited = []
        for cell in self.grid.each_cell():
            unvisited.append(cell)
        first = random.choice(unvisited)
        unvisited.remove(first)
        first.unvisited = False

        while unvisited != []:

            cell = random.choice(unvisited)
            path = [cell]

            while cell.unvisited:
                cell = random.choice(cell.neighbors())
                if cell in path:
                    path = path[0:path.index(cell)+1]
                else:
                    path.append(cell)

            for i in range(len(path)-1):
                path[i+1].link(path[i])
                path[i].unvisited = False
                unvisited.remove(path[i])

        return self.grid

class WilsonsExt:
    def __init__(self, grid):
        self.grid = grid

    def run(self):
        unvisited = {}
        path = []

        for cell in self.grid.each_cell():
            unvisited.update({cell: False})
            path.append(0)

        first = random.choice(list(unvisited.keys()))
        unvisited.pop(first)
        first.unvisited = False

        while unvisited != {}:
            #print(len(unvisited))
            cell = random.choice(list(unvisited.keys()))
            cell.step = 1
            path[0] = cell
            counter = 0

            while cell.unvisited:
                cell = random.choice(cell.neighbors())
                if cell.step < path[counter].step:

                    if cell.step != 0:
                        if path[cell.step - 1] != cell:  #Checked
                            counter += 1
                            cell.step = counter + 1
                            path[counter] = cell
                        else:                            #Checked
                            #print("else")
                            counter = cell.step - 1
                            cell = path[counter]
                    else:                                #Checked
                        counter += 1
                        cell.step = counter + 1
                        path[counter] = cell

                elif cell.step == path[counter].step:    #Checked
                    cell.step = 0
                    cell = path[counter]

                else:                                    # Checked
                    counter += 1
                    cell.step = counter + 1
                    path[counter] = cell
            for i in range(counter):
                #print(i)
                #print(path[i])
                path[i+1].link(path[i])
                path[i].unvisited = False
                unvisited.pop(path[i])
                #print(len(unvisited))

        print(totalTime)
        return self.grid
