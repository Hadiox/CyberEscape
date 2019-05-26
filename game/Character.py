import pygame
import os


class Character(object):
    run = [pygame.image.load(os.path.join('resources/character/run', 'run-' + str(x) + '.png')) for x in
           range(1, 8)]
    jump = [pygame.image.load(os.path.join('resources/character/jump','jump-'+str(x)+'.png')) for x in range(1,4)]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.longer_jumping = False
        self.jump_counter = 0
        self.run_counter = 0
        self.speed = 8
        self.hitbox = (self.x,self.y+20,width-20,height-20)
        self.longer_jump_list = [1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-3,-3,-3,-3,-3,-3,-3,-3,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        self.jump_list = [1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,-3,-3,-3,-3,-3,-3,-3,-3,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    def display(self, win):
        if self.longer_jumping:
            self.y -= self.longer_jump_list[self.jump_counter] * 5
            self.hitbox = (self.x, self.y + 20, self.width - 20, self.height - 20)
            win.blit(pygame.transform.scale(self.jump[(self.jump_counter // 30) - 1], (100, 100)), (self.x, self.y))
            self.jump_counter += 1
            if self.jump_counter>91:
                self.jump_counter = 0
                self.jumping = False
                self.longer_jumping = False
                self.run_counter = 0
        elif self.jumping:
            self.y -= self.jump_list[self.jump_counter]*5
            self.hitbox = (self.x,self.y+20,self.width-20,self.height-20)
            win.blit(pygame.transform.scale(self.jump[(self.jump_counter//18)-1],(100,100)),(self.x,self.y))
            self.jump_counter+=1
            if self.jump_counter == 32:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    self.longer_jumping = True
            if self.jump_counter>65:
                self.jump_counter = 0
                self.jumping = False
                self.run_counter = 0
        elif self.run_counter >= 7 * self.speed:
            self.run_counter = 0
        else:
            win.blit(pygame.transform.scale(self.run[self.run_counter // self.speed], (100, 100)), (self.x, self.y))
            self.run_counter += 1
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)