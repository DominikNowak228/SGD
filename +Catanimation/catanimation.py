import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Cat Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')


catx = 10
caty = 10
direction = 'right'


cat2x = 200
cat2y = 150
cat2dx = 3
cat2dy = 4

while True:
    DISPLAYSURF.fill(WHITE)

    # First cat
    if direction == 'right':
        catx += 5
        if catx >= 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty >= 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx <= 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty <= 10:
            direction = 'right'

    # Second cat movement
    cat2x += cat2dx
    cat2y += cat2dy

    if cat2x <= 0 or cat2x >= 400 - catImg.get_width():
        cat2dx = -cat2dx
    if cat2y <= 0 or cat2y >= 300 - catImg.get_height():
        cat2dy = -cat2dy

    # Draw both cats
    DISPLAYSURF.blit(catImg, (catx, caty))
    DISPLAYSURF.blit(catImg, (cat2x, cat2y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
