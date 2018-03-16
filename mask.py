import random

class Mask:
    def __init__(self, rows, columns):
        self.rows, self.columns = rows, columns
        self.bits = []
        for row in range(self.rows):
            columnList = []
            for col in range(self.columns):
                columnList.append({col: True})

            self.bits.append(columnList)

    def __getitem__(self, rowcol):
        row = rowcol[0]
        col = rowcol[1]
        if row in range(self.rows) and col in range(self.columns):
            return self.bits[row][col]
        else:
            False

    def __setitem__(self, rowcol, is_on):
        row = rowcol[0]
        col = rowcol[1]
        self.bits[row][col] = is_on

    def count(self):
        count = 0
        for row in range(self.rows): 
            for col in range(self.columns):
                if self.bits[row][col]:
                    count += 1 

        return count

    def random_location(self):
        row = random.randint(0, self.rows - 1)
        col = random.randint(0, self.columns - 1)
        if self.bits[row][col]:
            return [row, col]
        else:
            return self.random_location()

    def from_txt(self, file):
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

    

