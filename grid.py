import random
from PIL import Image, ImageDraw
from cell import Cell
import json

class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.cellsList = {}
        self.grid = self.prepare_grid()
        self.configure_cells()

    def __getitem__(self, coords):
        row, column = coords
        if row not in range(self.rows):
            return None 
        if column not in range(self.columns):
            return None
        
        return self.grid[row][column]

    def prepare_grid(self):
        for row in range(self.rows):
            columnList = {}
            for column in range(self.columns):
                cell = Cell(row, column)
                columnList.update({column: cell})
            self.cellsList.update({row: columnList})
        return self.cellsList

    def configure_cells(self):
        for row in self.cellsList:
            for col in self.cellsList[row]:
                cell = self.grid[row][col]
                if cell:
                    cell.west = self[[row, col - 1]]
                    cell.east = self[[row, col + 1]]
                    cell.north = self[[row - 1, col]]
                    cell.south = self[[row + 1, col]]

    def random_cell(self):
        row = random.randint(0, self.rows-1)
        column = random.randint(0, self.columns-1)

        return self.cellsList[row][column]

    def size(self):
        return self.rows * self.columns

    def each_row(self):
        for row in self.grid:
            yield self.grid[row]

    def each_cell(self):
        for row in self.each_row():
            for cell in row:
                if row[cell]:
                    yield row[cell]

    def deadends(self):
        array = []

        for cell in self.each_cell():
            if len(cell.links_list()) == 1:
                array.append(cell)

        return array

    def counter_junction(self, cell):
        number = [0, 0, 0, 0]
        if cell.east:
            if not cell.isLinked(cell.east):
                number[0] = 1
            if cell.east.south:
                if not cell.east.isLinked(cell.east.south):
                    number[1] += 1
        if cell.south:
            if not cell.isLinked(cell.south):
                number[3] = 1
            if cell.south.east:
                if not cell.south.isLinked(cell.south.east):
                    number[2] += 1
        return number

    def contents_of(self, cell):
        blank = " "
        return blank

    def background_color_for(self, cell):
        return None

    def __str__(self):
        output = "+" + "---+" * self.columns + "\n"
        for row in self.each_row():
            top = "|"
            bottom = "+"

            for col in row:
                cell = row[col]
                if not cell:
                    cell = Cell(-1, -1)
                body = " {} ".format(self.contents_of(cell))
                if cell.isLinked(cell.east):
                    east_boundary = " "
                else:
                    east_boundary = "|"
                top = top + body + east_boundary

                if cell.isLinked(cell.south):
                    south_boundary = "   "
                else:
                    south_boundary = "---"

                corner = "+"
                bottom = bottom + south_boundary + corner
            output = output + top + "\n" + bottom + "\n"
        return output

    def to_png(self, cell_size=10, mode="backgrounds"):
        img_width = cell_size * self.columns
        img_height = cell_size * self.rows
        background = "#ffffff"
        wall = "black"

        img = Image.new("RGBA", (img_width + 1, img_height + 1), background)
        for modes in [mode, "wall"]:
            for cell in self.each_cell():
                x1 = cell.column * cell_size
                y1 = cell.row * cell_size
                x2 = (cell.column + 1) * cell_size
                y2 = (cell.row + 1) * cell_size

                draw = ImageDraw.Draw(img)

                if modes == "backgrounds":
                    color = self.background_color_for(cell)
                    if color:
                        draw.rectangle([x1, y1, x2, y2], color, color)
                else:
                    if not cell.north:
                        draw.line((x1, y1, x2, y1), fill=wall)
                    if not cell.west:
                        draw.line((x1, y1, x1, y2), fill=wall)

                    if not cell.isLinked(cell.east):
                        draw.line((x2, y1, x2, y2), fill=wall)
                    if not cell.isLinked(cell.south):
                        draw.line((x1, y2, x2, y2), fill=wall)

                del draw

        img.save("test.png", "png")

    def to_img(self, formated="png", cell_size=10):
        if formated == "png":
            self.to_png(cell_size)

    def appender(self, coordinates, id):
        return {'type': 'Feature', 
                            'geometry': {
                                'type': 'LineString',
                                'coordinates': coordinates},
                            'properties': {
                                'id': id
                            }}

    def to_geosjson(self, cell_size=1000):
        features = []
        xadd = 4386062
        yadd = 7556059
        id = 0
        for cell in self.each_cell():
            x1 = cell.column * cell_size + xadd
            y1 = -cell.row * cell_size + yadd
            x2 = (cell.column + 1) * cell_size + xadd
            y2 = -(cell.row + 1) * cell_size + yadd
            if not cell.north:
                coordinates = [[x1, y1],[x2, y1]]
                features.append(self.appender(coordinates, id))
            if not cell.west:
                coordinates = [[x1, y1], [x1, y2]]
                features.append(self.appender(coordinates, id))
            if not cell.isLinked(cell.east):
                coordinates = [[x2, y1], [x2, y2]]
                features.append(self.appender(coordinates, id))
            if not cell.isLinked(cell.south):
                coordinates = [[x1, y2], [x2, y2]]
                features.append(self.appender(coordinates, id))
            id += 1
        featCollection = {'type': 'FeatureCollection', 'features': features}
        jstr = json.dumps(featCollection)
        with open("maze.json", 'w') as file:
            file.write(jstr)
        
