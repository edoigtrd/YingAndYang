import os
import pygame
from pygame.locals import *

class asset :
    def __init__(self, filename):
        if not os.path.isfile(filename):
            raise FileNotFoundError(filename)
        self.filename = filename
        self.name = filename.split('/')[-1].split('.')[0]
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.width, self.height = self.rect.size
        self.rect.center = (self.width / 2, self.height / 2)

    def resize(self,width,height):
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.width, self.height = self.rect.size
        self.rect.center = (self.width / 2, self.height / 2)

class assets_collection :
    def __init__(self):
        self.assets = []
        self.names = []
        self.macros = {}
    def __getitem__(self, name):
        if name in self.macros.keys():
            name = self.macros[name]
        for i in self.assets:
            if i.name == name:
                return i
        raise KeyError(name)
    def append(self, asset):
        self.assets.append(asset)
        self.names.append(asset.name)

    def set_macro(self, macro, name):
        if not name in self.names:
            raise KeyError(name)
        self.macros[macro] = name

    def get_macros(self):
        return self.macros

    def __iter__(self):
        return iter(self.assets)

assets = assets_collection()

for i in os.listdir('assets'):
    if i.endswith('.png'):
        print(f"Loading asset: {i}")
        assets.append(asset('assets/' + i))

assets.set_macro("#", "wall")
