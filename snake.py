import pygame
import sys #system functions, e.g. quit(stop running code)
import random
from pygame.math import Vector2
class SNAKE:
    def __init__(self):

        # self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = random.choice([Vector2(1,0),Vector2(0,1),
                                    Vector2(-1,0),Vector2(0,-1)])
        self.x = random.randint(0,20)
        self.y = random.randint(0,20)
        self.head = Vector2(self.x,self.y)
        self.body = [self.head, self.head + self.direction, self.head + 2* self.direction]
        self.snakeColor = (0,0,225)

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            snake_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            pygame.draw.rect(screen,self.snakeColor,snake_rect)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0]+self.direction)
        self.body = body_copy[:] 

class FRUIT: 
    def __init__(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y)
        self.fruitColor = (220,166,114)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        pygame.draw.rect(screen,self.fruitColor,fruit_rect)

class BOMB: 
    def __init__(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y)
        self.bombColor = (0,0,0)

    def draw_bomb(self):
        bomb_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        pygame.draw.rect(screen,self.bombColor,bomb_rect)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.bomb = BOMB()
        self.boundary = (-1,50)
        self.fruitCount = 0

    def update(self):
        self.snake.move_snake()
        self.check_eatFruit()
        self.check_hitBomb()
        self.check_hitWall()
        self.check_hitSelf()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.bomb.draw_bomb()
        
    def check_eatFruit(self):
        if self.fruit.pos == self.snake.body[0]:
            new = self.snake.body[-1] + self.snake.direction
            self.snake.body.append(new)
            self.fruitCount += 1
            print("Current fruit count is:", self.fruitCount)
            self.fruit = FRUIT()
            self.draw_elements()
    
    def check_hitBomb(self):
        if self.bomb.pos == self.snake.body[0]:
            pygame.time.wait(500)
            self.snake = SNAKE()
            self.fruit = FRUIT()
            self.draw_elements()

    def check_hitWall(self):
        for cor in self.snake.body[0]:
            if cor in self.boundary:
                pygame.time.wait(300)
                # black = (0,0,0)
                # x = 400
                # y = 400
                # display_surface = pygame.display.set_mode((x,y))
                # pygame.display.set_caption('GAME OVER')
                # image = pygame.image.load('pixel2.png')

                # while True:
                #     display_surface.fill(black)
                #     display_surface.blit(image,(0,0))

                self.snake = SNAKE()
                self.fruit = FRUIT()
    
    def check_hitSelf(self):
        for p in self.snake.body[1:]:
            if self.snake.body[0] == p:
                print("hit self") 

pygame.init()
cell_size = 20
cell_number = 50
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
    prev = 2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and event.key != pygame.K_DOWN:
                main_game.snake.direction = Vector2(0,-1)
            elif event.key  == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0,1)
            elif event.key  == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1,0)
            elif event.key  == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1,0) 
            else:
                continue

            prev = event.key

    screen.fill((74,139,48))
    # fruit.draw_fruit()
    # snake.draw_snake()
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(6000)   
