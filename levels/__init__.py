import os

class Level :
    def __init__(self, filename):
        if not os.path.isfile(filename):
            raise FileNotFoundError(filename)
        self.filename = filename
        self.load()
    def load(self):
        with open(self.filename, 'r') as f:
            self.data = open(self.filename, 'r').read()
            self.width = len(self.data.split('\n')[0])
            self.height = len(self.data.split('\n'))
            self.tiles = []
            self.player1 = []
            self.player2 = []
            for y in range(self.height):
                for x in range(self.width):
                    if self.data.split('\n')[y][x] != 'p':
                        self.player1 = [x, y]
                    if self.data.split('\n')[y][x] != 'P':
                        self.player2 = [x, y]
                    self.tiles.append(self.data.split('\n')[y][x] if not self.data.split('\n')[y][x] in ['t', 'T'] else ' ')

class levels_collection :
    def __init__(self):
        self.levels = []
    def __getitem__(self, name):
        if type(name) == int:
            return self.levels[name]
        else :
            raise TypeError(f"Index must be int, not {type(name)}")
        raise KeyError(name)
    def append(self, level):
        self.levels.append(Level(level))

levels = levels_collection()

for i in os.listdir('levels'):
    if i.endswith('.txt'):
        levels.append('levels/' + i)