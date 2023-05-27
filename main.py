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

def resize():
    for i in assets:
        i.resize(levels[current].get_ratio(screen), levels[current].get_ratio(screen))

def load():
    pygame.init()
    audios.play("music", True)
    pygame.display.set_icon(assets["icon"].image)

def keyboard(k) :
    global current
    if k.type == pygame.KEYDOWN :
        m = False
        if k.key in [pygame.K_LEFT, pygame.K_q] :
            m = [-1,0]
        if k.key in [pygame.K_RIGHT, pygame.K_d] :
            m = [1,0]
        if k.key in [pygame.K_UP, pygame.K_z] :
            m = [0,-1]
        if k.key in [pygame.K_DOWN, pygame.K_s] :
            m = [0,1]
        if k.key == pygame.K_SPACE :
            levels[current].load()
        if m :
            audios.play("oot")
            c = []
            levels[current].move(m,1)
            c.append(levels[current].check())
            levels[current].move(m,2)
            c.append(levels[current].check())
            if "gameover" in c :
                audios.play("lose")
                levels[current].load()
            if "win" in c :
                audios.play("win")
                current += 1
def update():
    global screen
    resize()


def draw():
    screen.fill(BLACK)
    l = levels[current]

    for x in range(l.width):
        for y in range(l.height):
            if l.tiles[y][x] == '#':
                screen.blit(assets['wall'].image, (x * assets["wall"].width + l.padx(screen), y * assets["wall"].height + l.pady(screen)))
            if l.tiles[y][x] == 't':
                screen.blit(assets["targetB"].image, (x * assets["targetB"].width + l.padx(screen), y * assets["targetB"].height + l.pady(screen)))
            if l.tiles[y][x] == 'T':
                screen.blit(assets["targetW"].image, (x * assets["targetW"].width + l.padx(screen), y * assets["targetW"].height + l.pady(screen)))
            if l.tiles[y][x] == '%':
                screen.blit(assets["stone"].image, (x * assets["stone"].width + l.padx(screen), y * assets["stone"].height + l.pady(screen)))
            if l.tiles[y][x] == 'x':
                screen.blit(assets["spike"].image, (x * assets["spike"].width + l.padx(screen), y * assets["spike"].height + l.pady(screen)))

    screen.blit(assets['playerW'].image,
                (l.player1[0] * assets["playerW"].width + l.padx(screen), l.player1[1] * assets["playerW"].height + l.pady(screen)))
    screen.blit(assets['playerB'].image,
                (l.player2[0] * assets["playerB"].width + l.padx(screen), l.player2[1] * assets["playerB"].height + l.pady(screen)))

    pygame.display.flip()

load()

running = True
while running :
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
        if events.type in [pygame.KEYUP, pygame.KEYDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN] :
            keyboard(events)
    update()
    draw()



pygame.quit()