import pygame
import os
import CyberEscape.game.Character


class Rectangle(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.id = 1
        self.height = height
        self.hitbox = (x, y, width, height)
        self.img = pygame.image.load(os.path.join('resources/obstacles', 'metalbox.png'))

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
        self.hitbox = (x, y, width, height)
        self.img = pygame.image.load(os.path.join('resources/obstacles', 'v-truck.png'))

    def draw(self, window):
        self.hitbox = (self.x, self.y, self.width, self.height)
        window.blit(pygame.transform.scale(self.img, (self.width, self.height)), (self.x, self.y))
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def collide(self, character):
        if self.x + self.width > character.x + character.hitbox[0] > self.x:
            if self.y + self.height > character.y + character.hitbox[1] > self.y:
                return True
        return False

class Police(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.id = 3
        self.height = height
        self.hitbox = (x, y, width, height)
        self.img = pygame.image.load(os.path.join('resources/obstacles', 'v-police.png'))

    def draw(self, window):
        self.hitbox = (self.x, self.y, self.width, self.height)
        window.blit(pygame.transform.scale(self.img, (self.width, self.height)), (self.x, self.y))
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def collide(self, character):
        if self.x + self.width > character.x + character.hitbox[0] > self.x:
            if self.y + self.height > character.y + character.hitbox[1] > self.y:
                return True
        return False

class Drone(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.id = 4
        self.height = height
        self.hitbox = (x, y, width, height)
        self.img = pygame.image.load(os.path.join('resources/obstacles', 'drone.png'))

    def draw(self, window):
        self.hitbox = (self.x, self.y, self.width, self.height)
        window.blit(pygame.transform.scale(self.img, (self.width, self.height)), (self.x, self.y))
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def collide(self, character):
        if self.x + self.width > character.x + character.hitbox[0] > self.x:
            if self.y + self.height > character.y + character.hitbox[1] > self.y:
                return True
        return False


class Rider(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.id = 5
        self.height = height
        self.hitbox = (x, y, width, height)
        self.img = pygame.image.load(os.path.join('resources/obstacles', 'rider.png'))

    def draw(self, window):
        self.hitbox = (self.x, self.y, self.width, self.height)
        window.blit(pygame.transform.scale(self.img, (self.width, self.height)), (self.x, self.y))
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def collide(self, character):
        if self.x + self.width > character.x + character.hitbox[0] > self.x:
            if self.y + self.height > character.y + character.hitbox[1] > self.y:
                return True
        return False


