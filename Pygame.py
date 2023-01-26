import pygame, sys

pygame.init()
screen = pygame.display.set_mode((500,600))
clock = pygame.time.Clock()
test_surface = pygame.Surface((100,200))
test_surface.fill(('green'))
test_rect = test_surface.get_rect(center = (250,250))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        screen.fill(pygame.Color(70,70,215))
        test_rect.right += 1
        screen.blit(test_surface,test_rect)
        pygame.display.update()
        clock.tick(60)




        def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            pygame.draw.rect(screen,(183,191,122),block_rect)





            self.head_up = pygame.image.load('imagies/head_up.jpg').convert_alpha()
        self.head_down = pygame.image.load('imagies/head_down.jpg').convert_alpha()
        self.head_right = pygame.image.load('imagies/head_right.jpg').convert_alpha()
        self.head_left = pygame.image.load('imagies/head_left.jpg').convert_alpha()



        self.tail_up = pygame.image.load('imagies/tail_up.jpg').convert_alpha()
        self.tail_down = pygame.image.load('imagies/tail_down.jpg').convert_alpha()
        self.tail_right = pygame.image.load('imagies/tail_right.jpg').convert_alpha()
        self.tail_left = pygame.image.load('imagies/tail_left.jpg').convert_alpha()



        self.body_vertical = pygame.image.load('imagies/body_vertical.jpg').convert_alpha()
        self.body_horizontal = pygame.image.load('imagies/body_horizontal.jpg').convert_alpha()

        self.body_tr = pygame.image.load('imagies/body_tr.jpg').convert_alpha()
        self.body_tl = pygame.image.load('imagies/body_tl.jpg').convert_alpha()
        self.body_br = pygame.image.load('imagies/body_br.jpg').convert_alpha()
        self.body_bl = pygame.image.load('imagies/body_bl.jpg').convert_alpha()



        if index == 0:
                screen.blit(self.head_up,block_rect)
            else:
                pygame.draw.rect(screen,(183,191,122),block_rect)





                self.head_up = pygame.image.load('imagies/head_up.jpg').convert_alpha()
        self.head_down = pygame.image.load('imagies/head_down.jpg').convert_alpha()
        self.head_right = pygame.image.load('imagies/head_right.jpg').convert_alpha()
        self.head_left = pygame.image.load('imagies/head_left.jpg').convert_alpha()



        self.tail_up = pygame.image.load('imagies/tail_up.jpg').convert_alpha()
        self.tail_down = pygame.image.load('imagies/tail_down.jpg').convert_alpha()
        self.tail_right = pygame.image.load('imagies/tail_right.jpg').convert_alpha()
        self.tail_left = pygame.image.load('imagies/tail_left.jpg').convert_alpha()



        self.body_vertical = pygame.image.load('imagies/body_vertical.jpg').convert_alpha()
        self.body_horizontal = pygame.image.load('imagies/body_horizontal.jpg').convert_alpha()

        self.body_tr = pygame.image.load('imagies/body_tr.jpg').convert_alpha()
        self.body_tl = pygame.image.load('imagies/body_tl.jpg').convert_alpha()
        self.body_br = pygame.image.load('imagies/body_br.jpg').convert_alpha()
        self.body_bl = pygame.image.load('imagies/body_bl.jpg').convert_alpha()
        self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')
    
    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()


        for index,block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)



            if index == 0:
                screen.blit(self.head_up,block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail,block_rect)

            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl,block_rect)
                    if previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl,block_rect)
                    if previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr,block_rect)
                    if previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_bl,block_rect)


    def update_head_graphics(self):
        head_relation = self.body[1] -self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down


    def update_tail_graphics(self):
        tail_relation = self.body[-2] -self.body[-1]
        if tail_relation == Vector2(): self.tail = self.tail_left
        elif tail_relation == Vector2(): self.tail = self.tail_left
        elif tail_relation == Vector2(): self.tail = self.tail_left
        elif tail_relation == Vector2(): self.tail = self.tail_left