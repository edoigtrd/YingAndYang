import pygame
from pygame.locals import *
import os
import config
from levels import levels
from assets import assets
from sound import audios
from stopwatch import *
from config import config
import threading

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("YingAndYang")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

current = 0


def load():
    pygame.init()
    audios.play("music", True)


def update():
    global screen
    print("Updating")
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
        if event.type == pygame.FULLSCREEN:
            screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        if event.type == pygame.KEYDOWN :
            print(event.key)
    resize()


def resize():
    for i in assets:
        i.resize(levels[current].get_ratio(screen), levels[current].get_ratio(screen))


def draw():
    print("Drawing")
    screen.fill(BLACK)
    l = levels[current]

    for x in range(l.width):
        for y in range(l.height):
            if l.tiles[y][x] == '#':
                screen.blit(assets['wall'].image, (x * assets["wall"].width + l.padx(screen), y * assets["wall"].height + l.pady(screen)))

    screen.blit(assets['playerW'].image,
                (l.player1[0] * assets["playerW"].width + l.padx(screen), l.player1[1] * assets["playerW"].height + l.pady(screen)))
    screen.blit(assets['playerB'].image,
                (l.player2[0] * assets["playerB"].width + l.padx(screen), l.player2[1] * assets["playerB"].height + l.pady(screen)))
    pygame.display.flip()


load()

update_thread = threading.Thread(target=update)
draw_thread = threading.Thread(target=draw)

running = True
while running :
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()


pygame.quit()