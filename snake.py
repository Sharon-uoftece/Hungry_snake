import pygame
import sys #system functions, e.g. quit(stop running code)
import random
from pygame.math import Vector2
class SNAKE:
    def __init__(self):

        # self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = random.choice([Vector2(1,0),Vector2(0,1),
                                    Vector2(-1,0),Vector2(0,-1)])
        self.x = random.randint(10,18)
        self.y = random.randint(10,18)
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
        screen.blit(apple,fruit_rect)
        #pygame.draw.rect(screen,self.fruitColor,fruit_rect)

class BOMB: 
    def __init__(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y)
        self.image = pygame.image.load('bomb.png')
        self.bombColor = (0,0,0)

    def draw_bomb(self,screen):
        # display_surface.fill((0,0,0))
        # pygame.display.set_caption('GAME OVER')
        # image = pygame.image.load('bomb.png')
        # screen.blit(image,(0,0))

        bomb_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        screen.blit(bomb,bomb_rect)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.bomb = BOMB()
        self.boundary = (-1,20)
        self.fruitCount = 0
        self.screen = pygame.display.set_mode((screen_width,screen_width))

    def update(self):
        self.snake.move_snake()
        self.check_eatFruit()
        self.check_hitBomb()
        self.check_hitWall()
        self.check_hitSelf()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.bomb.draw_bomb(self.screen)
        
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
            self.gameOver()
            self.snake = SNAKE()
            self.fruit = FRUIT()

    def check_hitWall(self):
        for cor in self.snake.body[0]:
            if cor in self.boundary:
                print(self.snake.body[0])
                self.gameOver()
                self.snake = SNAKE()
                self.fruit = FRUIT()
    
    def check_hitSelf(self):
        for p in self.snake.body[1:]:
            if self.snake.body[0] == p:
                continue

    def gameOver(self):
        pygame.time.wait(700)
        color = (255, 255, 255)
        display_surface = pygame.display.set_mode((screen_width, screen_width))
        pygame.display.set_caption('GAME OVER')
        image = pygame.image.load('gg.png')
        image_rect = image.get_rect()
        screen_rect = screen.get_rect()
        image_rect.center = screen_rect.center
        temp = 45000
        while temp > 0:
            display_surface.fill(color)
            display_surface.blit(image, image_rect)
            temp -= 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                        
                pygame.display.update()


pygame.init()
cell_size = 20
cell_number = 20
screen_width = cell_size * cell_number
screen = pygame.display.set_mode((screen_width,screen_width))
clock = pygame.time.Clock()
apple = pygame.image.load('apple.png').convert_alpha()
bomb = pygame.image.load('bomb.png').convert_alpha()

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
            if event.key == pygame.K_UP and event.key != pygame.K_DOWN:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            elif event.key  == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            elif event.key  == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
            elif event.key  == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0) 
            else:
                continue

    screen.fill((74,140,56))
    # fruit.draw_fruit()
    # snake.draw_snake()
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(600)   
