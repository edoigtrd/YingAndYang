import os
import toml

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

    def __str__(self):
        return str(self.tiles)