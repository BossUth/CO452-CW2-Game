from ctypes.wintypes import SIZE
import pygame
from pygame.locals import *
import time

class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("imagies/block.jpg").convert()
        self.x = [SIZE]*length
        self.y = [SIZE]*length

    def draw(self, surface):
        self.parent_screen.fill((43, 24, 135))
        self.parent_screen.blit(self.block,(self.x,self.y))
        pygame.display.flip()
    
    def move_up(self):
        self.direction = "up"
    
    def move_down(self):
        self.direction = "down"
     

    def move_left(self):
        self.direction = "left"
    
    
    def move_right(self):
        self.direction = "right"
    
    
    def walk(self):
        if self.direction == "up":
            self.y -= 10

        if self.direction == "down":
            self.y += 10
        
        if self.direction == "right":
            self.x += 10
        
        if self.direction == "left":
            self.y -= 10
        
        self.draw()
    

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 600))
        self.surface.fill((43, 24, 135))
        self.snake = Snake(self.surface)
        self.snake.draw

    def run(self):
        pass


    running = True

    while running:
     def __init__(self):
        pass
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    runnig = False

                if event.key == K_UP:
                  self.snake.move_up()
                    
                if event.key == K_DOWN:
                  self.snake.move_down()
                    
                if event.key == K_LEFT:
                  self.snake.move_left()
                  
                if event.key == K_RIGHT:
                  self.snake.move_right()

                
            elif event.type == QUIT:
                running = False
   
        
        self.snake.walk()
        time.sleep(0.2)


if __name__ == "__main__":
    game = Game()
    game.run()
        
