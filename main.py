import pygame
from pygame.locals import *

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("YingAndYang")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def update(events):
    pass

def draw():
    screen.fill(BLACK)
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

game_loop()
