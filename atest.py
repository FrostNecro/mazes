class tested():
    def __init__(self, item):
        self.item = item

    def __getitem__(self, item):
        return item[0]

Tested = tested([0, 1])
print(Tested[[2, 1]])
