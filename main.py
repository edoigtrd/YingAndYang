import pygame
from pygame.locals import *
import os
from levels import levels
from assets import assets

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("YingAndYang")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


current = 0

def load() :
    pass
def update(events):
    pass

def draw():
    screen.fill(BLACK)
    l = levels[current]
    for y in range(l.height):
        for x in range(l.width):
            if l.tiles[y * l.width + x] == '#':
                screen.blit(assets['wall'].image, (x * 16, y * 16))
    screen.blit(assets['playerB'].image, (l.player1[0] * 16, l.player1[1] * 16))
    screen.blit(assets['playerW'].image, (l.player2[0] * 16, l.player2[1] * 16))
    pygame.display.flip()

def game_loop():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        update(pygame.event.get())
        draw()

    pygame.quit()

load()
game_loop()
