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
        self.x = random.randint(0,cell_number-5)
        self.y = random.randint(0,cell_number-5)
        self.pos = Vector2(self.x,self.y)
        self.ran = random.randint(0,5)

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

class BOMB: 
    def __init__(self):
        self.x = random.randint(8,14)
        self.y = random.randint(8,14)
        self.pos = Vector2(self.x,self.y)
        self.image = pygame.image.load('bomb.png')
        self.bombColor = (0,0,0)

    def draw_bomb(self):
        bomb_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        screen.blit(bomb,bomb_rect)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit  = FRUIT()
        self.fruit2 = FRUIT()
        self.fruit3 = FRUIT() 
        self.bomb = BOMB()
        self.boundary = (-1,cell_number)
        self.screen = pygame.display.set_mode((screen_width,screen_width))

    def update(self):
        self.snake.move_snake()
        self.check_eatFruit()
        self.check_hitBomb()
        self.check_hitWall()
        self.check_hitSelf()
        self.draw_score()
        self.check_visibility()
        self.random_bomb()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.fruit2.draw_fruit()
        self.fruit3.draw_fruit()
        self.snake.draw_snake()
        self.bomb.draw_bomb()
        self.draw_score()

    def draw_score(self):
        score_text = str(len(self.snake.body)-3)
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x = int(cell_size * cell_number - 20)
        score_y = int(cell_size * cell_number - 20)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))
        heart_rect = apple.get_rect(midright = (score_rect.left+100,score_rect.centery+100))
        bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width+score_rect.width,apple_rect.height)
        
        pygame.draw.rect(screen,(167,209,61),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(heart,heart_rect)
        pygame.draw.rect(screen,(56,74,12),bg_rect,2)

    def check_eatFruit(self):
        if self.fruit == self.snake.body[0]:
            new = self.snake.body[-1] + self.snake.direction
            self.snake.body.append(new)
            time.sleep(999999)
            self.fruit = FRUIT()
        if self.fruit2 == self.snake.body[0]:
            new = self.snake.body[-1] + self.snake.direction
            self.snake.body.append(new)
            time.sleep(999999)
            self.fruit2 = FRUIT()
        if self.fruit3 == self.snake.body[0]:
            new = self.snake.body[-1] + self.snake.direction
            self.snake.body.append(new)
            time.sleep(999999)
            self.fruit3 = FRUIT()
    
    def random_bomb(self):
        counter_bomb = 1000
        while counter_bomb > 1:
            if counter_bomb == 0:
                self.bomb = BOMB() 
                counter_bomb = 1000
            counter_bomb -= 1

    def check_visibility(self):
        if self.fruit.pos == self.bomb.pos:
            self.bomb = BOMB()
        for p in self.snake.body:
            if self.fruit.pos == p:
                self.fruit = FRUIT()
            if self.fruit2.pos == p:
                self.fruit2 = FRUIT()
            if self.fruit3.pos == p:
                self.fruit3 = FRUIT()
            if self.bomb.pos == p:
                self.bomb = BOMB()
        # counter_visibility = 50
        # while counter_visibility > 0:
        #     counter_visibility -= 1
        #     print("counter visibility:",counter_visibility)
        #     if counter_visibility == 0:
        #         self.fruit == FRUIT()
        #         counter_visibility = 50
    
    # def random_fruit(self):
    #     continue
        
    def check_hitBomb(self):
        if self.bomb.pos == self.snake.body[0]:
            self.gameOver()
            self.snake = SNAKE()
            self.fruit = FRUIT() 
            self.fruit2 = FRUIT()
            self.fruit3 = FRUIT()

    def check_hitWall(self):
        for cor in self.snake.body[0]:
            if cor in self.boundary:
                print(self.snake.body[0])
                self.gameOver()
                self.snake = SNAKE()
                self.fruit = FRUIT()
                self.fruit2 = FRUIT()
                self.fruit3 = FRUIT()
    
    def check_hitSelf(self):
        for p in self.snake.body[1:]:
            if self.snake.body[0] == p:
                continue

    def gameOver(self):
        pygame.time.wait(700)
        color = (0,0,0)
        display_surface = pygame.display.set_mode((screen_width, screen_width))
        pygame.display.set_caption('GAME OVER')
        image = pygame.image.load('gg2.png').convert_alpha()
        image_rect = image.get_rect()
        screen_rect = screen.get_rect()
        image_rect.center = screen_rect.center
        temp = 10000
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
cherry = pygame.image.load('cherry.png').convert_alpha()
avocado = pygame.image.load('avocado.png').convert_alpha()
yuzu = pygame.image.load('yuzu.png').convert_alpha()
carrott = pygame.image.load('carrott.png').convert_alpha()
banana = pygame.image.load('banana.png').convert_alpha()
bomb = pygame.image.load('bomb.png').convert_alpha()
heart = pygame.image.load('heart.png').convert_alpha()
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
