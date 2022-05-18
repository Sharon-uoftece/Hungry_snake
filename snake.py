import pygame
import sys #system functions, e.g. quit(stop running code)
import random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.direction = random.choice([Vector2(1,0),Vector2(0,1),Vector2(-1,0),Vector2(0,-1)])
        self.x = random.randint(8,14)
        self.y = random.randint(8,14)
        self.head = Vector2(self.x,self.y)
        self.body = [self.head, self.head + self.direction, self.head + 2* self.direction]
        self.snakeColor = (120,120,220)

    def draw_snake(self):
        for block in self.body:
            x = int(block.x * cell_size)
            y = int(block.y * cell_size)
            block_rect = pygame.Rect(x,y,cell_size,cell_number)
            pygame.draw.rect(screen,self.snakeColor,block_rect)

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
        self.name = ""

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        if self.ran == 0:
            screen.blit(apple,fruit_rect)
            self.name = "apple"
        elif self.ran == 1:
            screen.blit(cherry,fruit_rect)
            self.name = "cherry"
        elif self.ran == 2:
            screen.blit(yuzu,fruit_rect)
            self.name = "yuzu"
        elif self.ran == 3:
            screen.blit(avocado,fruit_rect)
            self.name = "avocado"
        elif self.ran == 4:
            screen.blit(carrott,fruit_rect)
            self.name = "carrott"
        elif self.ran == 5:
            screen.blit(banana,fruit_rect)
            self.name = "banana"
        elif self.ran == 6:
            screen.blit(heart,fruit_rect)
            self.name = "heart"
        elif self.ran == 7:
            screen.blit(heart2,fruit_rect)
            self.name = "heart"
        elif self.ran == 8:
            screen.blit(heart3,fruit_rect)
            self.name = "heart"

class BOMB: 
    def __init__(self):
        self.x = random.randint(4,17)
        self.y = random.randint(4,17)
        self.pos = Vector2(self.x,self.y)
        self.ran = random.randint(0,3)
        self.name = ""
         
    def draw_bomb(self):
        bomb_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        if self.ran == 0:
            screen.blit(bomb,bomb_rect)
            self.name = "bomb"
        elif self.ran == 1:
            screen.blit(skull,bomb_rect)
            self.name = "skull"
        elif self.ran == 2:
            screen.blit(poison,bomb_rect)
            self.name = "poison"
        elif self.ran == 3:
            screen.blit(poison2,bomb_rect)
            self.name = "poison"

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit  = FRUIT()
        self.fruit2 = FRUIT()
        self.fruit3 = FRUIT() 
        self.fruits = [self.fruit,self.fruit2,self.fruit3]
        self.bomb = BOMB()
        self.bomb2 = BOMB()
        self.bomb3 = BOMB()
        self.bomb4 = BOMB()
        self.bombs = [self.bomb,self.bomb2,self.bomb3,self.bomb4]
        self.boundary = (-1,cell_number)
        self.screen = pygame.display.set_mode((screen_width,screen_width))

    def update(self):
        self.snake.move_snake()
        self.check_eatFruit()
        self.check_hitBomb()
        self.check_hitWall()
        self.check_hitSelf()
        self.check_visibility()
        self.randomize_Bomb()
        self.randomize_Fruit()
        self.draw_score()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.fruit2.draw_fruit()
        self.fruit3.draw_fruit()
        self.bomb.draw_bomb()
        self.bomb2.draw_bomb()
        self.bomb3.draw_bomb()
        self.bomb4.draw_bomb()
        self.snake.draw_snake()
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
        score_surface = game_font.render(score_text,True,(36,94,12))
        score_x = int(cell_size * cell_number - 30)
        score_y = int(cell_size * cell_number - 30)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        screen.blit(score_surface,score_rect)

    def check_eatFruit(self):
        if self.snake.body[0] == self.fruit.pos: 
            self.check_Fruit(self.fruit)
            self.fruit = FRUIT()
        elif self.snake.body[0] == self.fruit2.pos:
            self.check_Fruit(self.fruit2)
            self.fruit2 = FRUIT()
        elif self.snake.body[0] == self.fruit3.pos:
            self.check_Fruit(self.fruit3)
            self.fruit3 = FRUIT()

    def check_Fruit(self,fruit):
        if fruit.name == "heart": 
            for i in range(3):
                new = self.snake.body[-1] + self.snake.direction
                self.snake.body.append(new)
                i += 1
        else: 
            new = self.snake.body[-1] + self.snake.direction
            self.snake.body.append(new)

    ####### NEED TO FIX########
    def check_visibility(self): 
        check_Fruit = []
        check_Bomb = []
        for f in self.fruits:
            for b in self.bombs:
                if tuple(f.pos) == tuple(b.pos):
                    f = FRUIT()
                if tuple(b.pos) in check_Bomb:
                    b = BOMB()
                check_Bomb.append(tuple(b.pos))
            if tuple(f.pos) in check_Fruit:
                f = FRUIT() 

    def check_hitBomb(self):
        if self.snake.body[0] == self.bomb.pos:
            self.check_Bomb(self.bomb)
            self.bomb = BOMB()
        if self.snake.body[0] == self.bomb2.pos:
            self.check_Bomb(self.bomb2)
            self.bomb2 = BOMB()
        if self.snake.body[0] == self.bomb3.pos:
            self.check_Bomb(self.bomb3)
            self.bomb3 = BOMB()
        if self.snake.body[0] == self.bomb4.pos:
            self.check_Bomb(self.bomb4)
            self.bomb4 = BOMB()

    def check_Bomb(self,bomb):
        if bomb.name == "bomb":
            pygame.time.wait(600) 
            self.gameOver()
            self.reinitialize()
        elif bomb.name == "poison":
            if len(self.snake.body) >= 5:
                temp_body = self.snake.body[:-3]
                self.snake.body = temp_body
            else:
                self.gameOver()
                self.reinitialize()
        elif bomb.name == "skull":
            pygame.time.wait(700) 
            bomb = BOMB()
            if self.snake.body[0].y >= cell_number - 5 and self.snake.direction != Vector2(0,1):
                new_direction = Vector2(0,-1) #up
            elif self.snake.body[0].y < 5 and self.snake.direction != Vector2(1,0):
                new_direction = Vector2(0,1) #down 
            elif self.snake.body[0].x >= cell_number - 5 and self.snake.direction != Vector2(1,0):
                new_direction = Vector2(-1,0) #left
            elif self.snake.body[0].x < 5 and self.snake.direction != Vector2(-1,0):
                new_direction = Vector2(1,0) #right
            else:
                new_x = self.snake.direction[1]
                new_y = self.snake.direction[0]
                new_direction = Vector2(new_x,new_y)

            self.snake.direction = new_direction
             
    def check_hitWall(self):
        for cor in self.snake.body[0]:
            if cor in self.boundary:
                self.gameOver()
                self.reinitialize()

    def randomize_Fruit(self):
        snake_x = self.snake.body[0][0]
        snake_y = self.snake.body[0][1]
        if snake_x == self.fruit.pos.x + 2 and snake_y == self.fruit.pos.y + 2:
            self.fruit = FRUIT()
        if snake_x == self.fruit2.pos.x + 2 and snake_y == self.fruit2.pos.y - 2:
            self.fruit2 = FRUIT()
        if snake_x == self.fruit3.pos.x - 2 and snake_y == self.fruit3.pos.y + 2:
            self.fruit3 = FRUIT()
    
    def randomize_Bomb(self):
        snake_x = self.snake.body[0][0]
        snake_y = self.snake.body[0][1]
        if snake_x == self.bomb.pos.x + 2 and snake_y == self.bomb.pos.y + 2:
            self.bomb = BOMB()
        if snake_x == self.bomb2.pos.x - 2 and snake_y == self.bomb2.pos.y - 2:
            self.bomb2 = BOMB()
        if snake_x == self.bomb3.pos.x + 1 and snake_y == self.bomb3.pos.y + 1:
            self.bomb3 = BOMB()
        if snake_x == self.bomb4.pos.x - 1 and snake_y == self.bomb4.pos.y - 1:
            self.bomb4 = BOMB()

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
    
    def check_hitSelf(self):
        index = 1
        for p in self.snake.body[3:]:
            if self.snake.body[0] == p:
                self.snake.body = self.snake.body[:index]
            index += 1

    def reinitialize(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.fruit2 = FRUIT()
        self.fruit3 = FRUIT()
        self.bomb = BOMB()
        self.bomb2 = BOMB()
        self.bomb3 = BOMB()
        self.bomb4 = BOMB()

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

head_up = pygame.image.load('head_up.png').convert_alpha()
head_down = pygame.image.load('head_down.png').convert_alpha()
head_left = pygame.image.load('head_left.png').convert_alpha()
head_right = pygame.image.load('head_right.png').convert_alpha()

body_horizontal = pygame.image.load('body_horizontal.png').convert_alpha()
body_vertical = pygame.image.load('body_vertical.png').convert_alpha()

tail_up = pygame.image.load('tail_up.png').convert_alpha()
tail_down = pygame.image.load('tail_down.png').convert_alpha()
tail_left = pygame.image.load('tail_left.png').convert_alpha()
tail_right = pygame.image.load('tail_right.png').convert_alpha()

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
            if event.key == pygame.K_UP:
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
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(6000000)   
