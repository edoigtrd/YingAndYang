import pygame

from assets import assets
from levels import levels
from sound import audios

pygame.init()

WIDTH = pygame.display.Info().current_w * 0.7
HEIGHT = pygame.display.Info().current_h * 0.7

current = 0

def resize():
    for i in assets:
        i.resize(levels[current].get_ratio(screen), levels[current].get_ratio(screen))


def load():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    audios.play("music", True)
    pygame.display.set_caption("YingAndYang", "assets/icon.png")
    pygame.display.set_icon(assets["icon"].image)
    pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)


def keyboard(k):
    global current
    if k.type == pygame.KEYDOWN:
        m = False
        if k.key in [pygame.K_LEFT, pygame.K_q]:
            m = [-1, 0]
        if k.key in [pygame.K_RIGHT, pygame.K_d]:
            m = [1, 0]
        if k.key in [pygame.K_UP, pygame.K_z]:
            m = [0, -1]
        if k.key in [pygame.K_DOWN, pygame.K_s]:
            m = [0, 1]
        if k.key == pygame.K_SPACE:
            levels[current].load()
        if k.key == pygame.K_F11 :
            if screen.get_flags() & pygame.FULLSCREEN:
                pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            else:
                pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        if m:
            audios.play("oot")
            c = []
            levels[current].move(m, 1)
            c.append(levels[current].check())
            levels[current].move(m, 2)
            c.append(levels[current].check())
            if "win" == c[1]:
                audios.play("win")
                current += 1
            if "gameover" in c:
                audios.play("lose")
                levels[current].load()


def update():
    global screen
    resize()


def draw():
    screen.fill((0,0,0))
    l = levels[current]

    for x in range(l.width):
        for y in range(l.height):
            if l.tiles[y][x] == '#':
                screen.blit(assets['wall'].image,
                            (x * assets["wall"].width + l.padx(screen), y * assets["wall"].height + l.pady(screen)))
            if l.tiles[y][x] == 't':
                screen.blit(assets["targetB"].image, (
                    x * assets["targetB"].width + l.padx(screen), y * assets["targetB"].height + l.pady(screen)))
            if l.tiles[y][x] == 'T':
                screen.blit(assets["targetW"].image, (
                    x * assets["targetW"].width + l.padx(screen), y * assets["targetW"].height + l.pady(screen)))
            if l.tiles[y][x] == '%':
                screen.blit(assets["stone"].image,
                            (x * assets["stone"].width + l.padx(screen), y * assets["stone"].height + l.pady(screen)))
            if l.tiles[y][x] == 'x':
                screen.blit(assets["spike"].image,
                            (x * assets["spike"].width + l.padx(screen), y * assets["spike"].height + l.pady(screen)))

    screen.blit(assets['playerW'].image,
                (l.player1[0] * assets["playerW"].width + l.padx(screen),
                 l.player1[1] * assets["playerW"].height + l.pady(screen)))
    screen.blit(assets['playerB'].image,
                (l.player2[0] * assets["playerB"].width + l.padx(screen),
                 l.player2[1] * assets["playerB"].height + l.pady(screen)))

    pygame.display.flip()


load()

running = True
while running:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
        if events.type in [pygame.KEYUP, pygame.KEYDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN]:
            keyboard(events)
    update()
    draw()

pygame.quit()
