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
        self.array = [self.hitbox, self.hitbox, self.hitbox, self.hitbox]
        self.img = pygame.image.load(os.path.join('resources/obstacles', 'v-truck.png'))

    def draw(self, window):
        self.array[0] = (self.x + 10, self.y + 130, self.width - 20, self.height - 100)
        pygame.draw.rect(window, (255, 0, 0), self.array[0], 2)

        self.array[1] = (self.x + 35, self.y + 70, self.width - 40, self.height - 140)
        pygame.draw.rect(window, (255, 0, 0), self.array[1], 2)

        self.array[2] = (self.x + 137, self.y + 35, self.width - 140, self.height - 150)
        pygame.draw.rect(window, (255, 0, 0), self.array[2], 2)

        self.array[3] = (self.x + 312, self.y, self.width - 342, self.height - 160)
        pygame.draw.rect(window, (255, 0, 0), self.array[3], 2)

        window.blit(pygame.transform.scale(self.img, (self.width, self.height)), (self.x, self.y))

    def collide(self, character):
        if (((self.array[0][1] > character.y + character.hitbox[1]) or (character.y  < self.array[0][1] + self.array[0][3]))
                and ((self.array[0][0] > character.x + character.hitbox[0]) or (character.x  > self.array[0][0] + self.array[0][2]))):
                return False
        elif (((self.array[1][1] > character.y + character.hitbox[1]) or (character.y  < self.array[1][1] + self.array[1][3]))
            and ((self.array[1][0] > character.x + character.hitbox[0]) or (character.x  > self.array[1][0] + self.array[1][2]))):
                return False
        elif(((self.array[2][1] > character.y + character.hitbox[1]) or (character.y < self.array[2][1] + self.array[2][3]))
            and ((self.array[2][0] > character.x + character.hitbox[0]) or (character.x > self.array[2][0] + self.array[2][2]))):
                return False
        elif (((self.array[3][1] > character.y + character.hitbox[1]) or (character.y < self.array[3][1] + self.array[3][3]))
              and ((self.array[3][0] > character.x + character.hitbox[0]) or (character.x > self.array[3][0] + self.array[3][2]))):
            return False
        else:
            return True

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
        self.array = [self.hitbox, self.hitbox, self.hitbox]
        self.img = pygame.image.load(os.path.join('resources/obstacles', 'drone.png'))

    def draw(self, window):
        self.array[0] = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(window, (255, 0, 0), self.array[0], 2)

        #self.array[1] = (self.x + 41, self.y, self.width - 40, self.height - 50)
       # pygame.draw.rect(window, (255, 0, 0), self.array[1], 2)

       # self.array[2] = (self.x + 12, self.y + 32, self.width - 150, self.height - 70)
       # pygame.draw.rect(window, (255, 0, 0), self.array[2], 2)

        window.blit(pygame.transform.scale(self.img, (self.width, self.height)), (self.x, self.y))

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
        self.array = [self.hitbox, self.hitbox, self.hitbox]
        self.img = pygame.image.load(os.path.join('resources/obstacles', 'rider.png'))

    def draw(self, window):
        self.array[0] = (self.x - 5, self.y + 50, self.width - 20, self.height - 50)
        pygame.draw.rect(window, (255, 0, 0), self.array[0], 2)

        self.array[1] = (self.x + 41, self.y, self.width - 40, self.height - 50)
        pygame.draw.rect(window, (255, 0, 0), self.array[1], 2)

        self.array[2] = (self.x + 12, self.y + 32, self.width - 150, self.height - 70)
        pygame.draw.rect(window, (255, 0, 0), self.array[2], 2)

        window.blit(pygame.transform.scale(self.img, (self.width, self.height)), (self.x, self.y))

    def collide(self, character):

        if (((self.array[0][1] > character.y + character.hitbox[1]) or (character.y  < self.array[0][1] + self.array[0][3]))
                and ((self.array[0][0] > character.x + character.hitbox[0]) or (character.x  > self.array[0][0] + self.array[0][2]))):
                return False
        elif (((self.array[1][1] > character.y + character.hitbox[1]) or (character.y  < self.array[1][1] + self.array[1][3]))
            and ((self.array[1][0] > character.x + character.hitbox[0]) or (character.x  > self.array[1][0] + self.array[1][2]))):
                return False
        elif(((self.array[2][1] > character.y + character.hitbox[1]) or (character.y < self.array[2][1] + self.array[2][3]))
            and ((self.array[2][0] > character.x + character.hitbox[0]) or (character.x > self.array[2][0] + self.array[2][2]))):
                return False
        else:
            return True







