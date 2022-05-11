import pygame
import sys #system functions, e.g. quit(stop running code)

pygame.init()

#initailize the display surface
screen = pygame.display.set_mode((400,500))
#initialize a clock and can later set to different parameter
#for purpose of uniforming running speed of game
#if tick(60), loop 60 times in one min
clock = pygame.time.Clock()
test_rect = pygame.Rect(100,200,100,100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((74,139,48))
    pygame.draw.rect(screen,pygame.Color('red'),test_rect)
    pygame.display.update()
    clock.tick(60)   