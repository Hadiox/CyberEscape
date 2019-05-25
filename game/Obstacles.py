import pygame
import os
import game.Character


class Rectangle(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.id = 1
        self.height = height
        self.hitbox = (x, y, width, height)
        self.img = pygame.image.load(os.path.join('resources/Ground', 'simple_ground.jpg'))

    def draw(self, window):
        self.hitbox = (self.x, self.y, self.width, self.height)
        window.blit(pygame.transform.scale(self.img, (self.width, self.height)), (self.x, self.y))
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def collide(self, character):
        if self.x + self.width > character.x + character.hitbox[0] > self.x:
            if self.y + self.height > character.y + character.hitbox[1] > self.y:
                return True
        return False

class Truck(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.id = 2
        self.height = height
        self.hitbox = (x, y+(height*2//3), width, height//3)
        self.img = pygame.image.load(os.path.join('resources/obstacles', 'v-truck.png'))

    def draw(self, window):
        self.hitbox = (self.x, self.y+ self.height//3, self.width, self.height//3)
        window.blit(pygame.transform.scale(self.img, (self.width, self.height)), (self.x, self.y))
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def collide(self, character):
        if self.x + self.width > character.x + character.hitbox[0] > self.x:
            if self.y + self.height > character.y + character.hitbox[1] > self.y:
                return True
        return False