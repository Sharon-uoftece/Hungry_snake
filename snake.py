import pygame
import sys #system functions, e.g. quit(stop running code)
import random
from pygame.math import Vector2
class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            snake_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            pygame.draw.rect(screen,(0,0,225),snake_rect)
    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0]+self.direction)
        self.body = body_copy[:] 

class FRUIT: 
    def __init__(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        pygame.draw.rect(screen,(220,166,114),fruit_rect)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()


    def update(self):
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            new = self.snake.body[-1] + self.snake.direction
            self.snake.body.append(new)
            self.fruit = FRUIT()
            self.draw_elements()

pygame.init()
cell_size = 40
cell_number = 20
screen_width = cell_size * cell_number

#initailize the display surface
screen = pygame.display.set_mode((screen_width,screen_width))
#initialize a clock and can later set to different parameter
#for purpose of uniforming running speed of game
#if tick(60), loop 60 times in one min
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150) 

main_game = MAIN()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0,-1)
            elif event.key  == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0,1)
            elif event.key  == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1,0)
            elif event.key  == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1,0) 
    screen.fill((74,139,48))
    # fruit.draw_fruit()
    # snake.draw_snake()
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)   

    #testing testing 