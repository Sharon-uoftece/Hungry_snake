import pygame
import sys #system functions, e.g. quit(stop running code)
import random
import time
from pygame.math import Vector2

class SNAKE:
    def __init__(self):

        # self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = random.choice([Vector2(1,0),Vector2(0,1),
                                    Vector2(-1,0),Vector2(0,-1)])
        self.x = random.randint(10,12)
        self.y = random.randint(10,12)
        self.head = Vector2(self.x,self.y)
        self.body = [self.head, self.head + self.direction, self.head + 2* self.direction]
        self.snakeColor = (120,120,220)
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
        self.list = list(range(0,cell_number-2))
        self.randInput = self.list[::2]
        self.x = random.choice(self.randInput)
        self.y = random.choice(self.randInput)
        self.pos = Vector2(self.x,self.y)
        self.ran = random.randint(0,8)
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        if self.ran == 0:
            screen.blit(apple,fruit_rect)
        elif self.ran == 1:
            screen.blit(cherry,fruit_rect)
        elif self.ran == 2:
            screen.blit(yuzu,fruit_rect)
        elif self.ran == 3:
            screen.blit(avocado,fruit_rect)
        elif self.ran == 4:
            screen.blit(carrott,fruit_rect)
        elif self.ran == 5:
            screen.blit(banana,fruit_rect)
        elif self.ran == 6:
            screen.blit(heart,fruit_rect)
        elif self.ran == 7:
            screen.blit(heart2,fruit_rect)
        elif self.ran == 8:
            screen.blit(heart3,fruit_rect)
class BOMB: 
    def __init__(self):
        self.x = random.randint(3,17)
        self.y = random.randint(3,17)
        self.pos = Vector2(self.x,self.y)
        self.ran = random.randint(0,3)
    def draw_bomb(self):
        bomb_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        if self.ran == 0:
            screen.blit(bomb,bomb_rect)
        elif self.ran == 1:
            screen.blit(skull,bomb_rect)
        elif self.ran == 2:
            screen.blit(poison,bomb_rect)
        elif self.ran == 3:
            screen.blit(poison2,bomb_rect)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit  = FRUIT()
        self.fruit2 = FRUIT()
        self.fruit3 = FRUIT() 
        self.bomb = BOMB()
        self.bomb2 = BOMB()
        self.boundary = (-1,cell_number)
        self.screen = pygame.display.set_mode((screen_width,screen_width))
    def update(self):
        self.snake.move_snake()
        self.check_eatFruit()
        self.check_hitBomb()
        self.check_hitWall()
        self.draw_score()
        self.check_visibility()
    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.fruit2.draw_fruit()
        self.fruit3.draw_fruit()
        self.snake.draw_snake()
        self.bomb.draw_bomb()
        self.bomb2.draw_bomb()
        self.draw_score()
    def draw_grass(self):
        grass_color = (160,225,185)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)                      
    def draw_score(self):
        score_text = str(len(self.snake.body)-3)
        score_surface = game_font.render(score_text,True,(56,94,12))
        score_x = int(cell_size * cell_number - 30)
        score_y = int(cell_size * cell_number - 30)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        screen.blit(score_surface,score_rect)
    def check_eatFruit(self):
        if self.snake.body[0] == self.fruit.pos: 
            if self.fruit.ran in [6,7,8]: 
                for i in range(3):
                    new = self.snake.body[-1] + self.snake.direction
                    self.snake.body.append(new)
                    i += 1
            else: 
                new = self.snake.body[-1] + self.snake.direction
                self.snake.body.append(new)
            self.fruit = FRUIT()
        elif self.snake.body[0] == self.fruit2.pos:
            if self.fruit.ran in [6,7,8]: 
                for i in range(3):
                    new = self.snake.body[-1] + self.snake.direction
                    self.snake.body.append(new)
                    i += 1
            else: 
                new = self.snake.body[-1] + self.snake.direction
                self.snake.body.append(new)
            self.fruit2 = FRUIT()
        elif self.snake.body[0] == self.fruit3.pos:
            if self.fruit.ran in [6,7,8]: 
                for i in range(3):
                    new = self.snake.body[-1] + self.snake.direction
                    self.snake.body.append(new)
                    i += 1
            else: 
                new = self.snake.body[-1] + self.snake.direction
                self.snake.body.append(new)
            self.fruit3 = FRUIT()
    def check_visibility(self):
        if self.fruit.pos == self.bomb.pos:
            self.bomb = BOMB()
            self.bomb2 = BOMB()
        if self.fruit2.pos == self.bomb.pos:
            self.bomb = BOMB()
            self.bomb2 = BOMB()
        if self.fruit3.pos == self.bomb.pos:
            self.bomb = BOMB()
            self.bomb2 = BOMB()
        for p in self.snake.body[1:]:
            if self.fruit.pos == p:
                self.fruit = FRUIT()
            if self.fruit2.pos == p:
                self.fruit2 = FRUIT()
            if self.fruit3.pos == p:
                self.fruit3 = FRUIT()
            if self.bomb.pos == p:
                self.bomb = BOMB() 
            if self.bomb2.pos == p:
                self.bomb2 = BOMB() 
    def check_hitBomb(self):
        snake_head_x = self.snake.body[0][0]
        snake_head_y = self.snake.body[0][1]
        bomb_x = self.bomb.pos[0]
        bomb_y = self.bomb.pos[0]
        bomb2_x = self.bomb2.pos[0]
        bomb2_y = self.bomb2.pos[0]

        if snake_head_x == bomb_x + 1 and snake_head_y == bomb_y + 1:
            self.bomb = BOMB()
        elif snake_head_x == bomb_x - 1 and snake_head_y == bomb_y - 1:
            self.bomb = BOMB()
        
        if snake_head_x == bomb2_x + 1 and snake_head_y == bomb2_y + 1:
            self.bomb2 = BOMB()
        elif snake_head_x == bomb2_x - 1 and snake_head_y == bomb2_y - 1:
            self.bomb2 = BOMB()
        
        if self.bomb.pos == self.snake.body[0]:
            self.gameOver()
            self.snake = SNAKE()
        
        if self.bomb2.pos == self.snake.body[0]:
            self.gameOver()
            self.snake = SNAKE()
        
    def check_hitWall(self):
        for cor in self.snake.body[0]:
            if cor in self.boundary:
                self.gameOver()
                self.snake = SNAKE()
    def gameStart(self):
        color = (0,0,0)
        display_surface = pygame.display.set_mode((screen_width, screen_width))
        pygame.display.set_caption('GAME START')
        image = pygame.image.load('opening.jpg').convert_alpha()
        image_rect = image.get_rect()
        screen_rect = screen.get_rect()
        image_rect.center = screen_rect.center
        temp = 10000
        while temp > 0:
            display_surface.fill(color)
            display_surface.blit(image, image_rect)
            temp -= 1
            for event in pygame.event.get():
                # if event.type == pygame.QUIT:
                    # pygame.quit()
                    # quit()   
                pygame.display.update()
    def gameOver(self):
        pygame.time.wait(700)
        color = (0,0,0)
        display_surface = pygame.display.set_mode((screen_width, screen_width))
        pygame.display.set_caption('GAME OVER')
        image = pygame.image.load('gg2.png').convert_alpha()
        image_rect = image.get_rect()
        screen_rect = screen.get_rect()
        image_rect.center = screen_rect.center
        temp = 19000
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
pygame.display.set_caption('Hungry Snake -- Game Start')
clock = pygame.time.Clock()

apple = pygame.image.load('apple.png').convert_alpha()
cherry = pygame.image.load('cherry.png').convert_alpha()
avocado = pygame.image.load('avocado.png').convert_alpha()
yuzu = pygame.image.load('yuzu.png').convert_alpha()
carrott = pygame.image.load('carrott.png').convert_alpha()
banana = pygame.image.load('banana.png').convert_alpha()
heart = pygame.image.load('heart.png').convert_alpha()
heart2 = pygame.image.load('heart2.png').convert_alpha()
heart3 = pygame.image.load('heart3.png').convert_alpha()
bomb = pygame.image.load('bomb.png').convert_alpha()
skull = pygame.image.load('skull.png').convert_alpha()
poison = pygame.image.load('poison.png').convert_alpha()
poison2 = pygame.image.load('poison2.png').convert_alpha()


game_font = pygame.font.Font('PoetsenOne-Regular.ttf',25)

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

    screen.fill((160,215,160))
    # fruit.draw_frui t()
    # snake.draw_snake()
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)   
