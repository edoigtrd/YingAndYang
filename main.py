import pygame
from pygame.locals import *
import os
import config
from levels import levels
from assets import assets
from stopwatch import *
from config import config


pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT) , pygame.RESIZABLE)
pygame.display.set_caption("YingAndYang")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


current = 0

def load() :
    pass
def update(events):
    global screen
    for event in events:
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)


def draw():
    screen.fill(BLACK)
    l = levels[current]
    for x in range(l.width):
        for y in range(l.height):
            if l.tiles[y][x] == '#':
                screen.blit(assets['wall'].image, (x * 16 + l.padx(screen), y * 16 + l.pady(screen)))
    screen.blit(assets['playerB'].image, (l.player1[0] * 16 + l.padx(screen), l.player1[1] * 16 + l.pady(screen)))
    screen.blit(assets['playerW'].image, (l.player2[0] * 16 + l.padx(screen), l.player2[1] * 16 + l.pady(screen)))
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
