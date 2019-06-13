import pygame
import os


class Rectangle(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.id = 1
        self.height = height
        self.hitbox = (x, y, width, height)
        self.array = [self.hitbox]
        self.img = pygame.image.load(os.path.join('../resources/obstacles', 'metalbox.png'))

    def draw(self, window):
        self.array[0] = (self.x, self.y, self.width, self.height)
        window.blit(pygame.transform.scale(self.img, (self.width, self.height)), (self.x, self.y))
        # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def collide(self, character):
        if not (((self.array[0][1] > character.hitbox[1] + character.hitbox[3]) or (
                character.hitbox[1] > self.array[0][1] + self.array[0][3]))
                or ((self.array[0][0] > character.hitbox[0] + character.hitbox[2]) or (
                        character.hitbox[0] > self.array[0][0] + self.array[0][2]))):
            return True

        return False


class Truck(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.id = 2
        self.height = height
        self.hitbox = (x, y + (height * 2 // 3), width, height // 3)
        self.array = [self.hitbox]
        self.img = pygame.image.load(os.path.join('../resources/obstacles', 'v-truck.png'))

    def draw(self, window):
        self.hitbox = (self.x, self.y + self.height // 3, self.width, self.height // 3)
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.array = [self.hitbox, self.hitbox, self.hitbox, self.hitbox]
        self.img = pygame.image.load(os.path.join('../resources/obstacles', 'v-truck.png'))
        window.blit(pygame.transform.scale(self.img, (self.width, self.height)), (self.x, self.y))

    def collide(self, character):
        if not (((self.array[0][1] > character.hitbox[1] + character.hitbox[3]) or (
                character.hitbox[1] > self.array[0][1] + self.array[0][3]))
                or ((self.array[0][0] > character.hitbox[0] + character.hitbox[2]) or (
                        character.hitbox[0] > self.array[0][0] + self.array[0][2]))):
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
        self.array = [self.hitbox, self.hitbox, self.hitbox, self.hitbox, self.hitbox]
        self.img = pygame.image.load(os.path.join('../resources/obstacles', 'v-police.png'))

    def draw(self, window):
        self.array[0] = (self.x, self.y + 70, self.width - 30, self.height - 70)
        # pygame.draw.rect(window, (255, 0, 0), self.array[0], 2)

        self.array[1] = (self.x + 46, self.y + 45, self.width - 56, self.height - 70)
        # pygame.draw.rect(window, (255, 0, 0), self.array[1], 2)

        self.array[2] = (self.x + 74, self.y + 25, self.width - 77, self.height - 70)
        # pygame.draw.rect(window, (255, 0, 0), self.array[2], 2)

        self.array[3] = (self.x + 100, self.y + 10, self.width - 137, self.height - 80)
        # pygame.draw.rect(window, (255, 0, 0), self.array[3], 2)

        self.array[4] = (self.x + 162, self.y, self.width - 228, self.height - 90)
        # pygame.draw.rect(window, (255, 0, 0), self.array[4], 2)

        window.blit(pygame.transform.scale(self.img, (self.width, self.height)), (self.x, self.y))

    def collide(self, character):
        for i in range(0, 5):
            if not (((self.array[i][1] > character.hitbox[1] + character.hitbox[3]) or (
                    character.hitbox[1] > self.array[i][1] + self.array[i][3]))
                    or ((self.array[i][0] > character.hitbox[0] + character.hitbox[2]) or (
                            character.hitbox[0] > self.array[i][0] + self.array[i][2]))):
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
        self.img = pygame.image.load(os.path.join('../resources/obstacles', 'drone.png'))

    def draw(self, window):
        self.array[0] = (self.x + 22, self.y + 30, self.width - 42, self.height - 40)
        # pygame.draw.rect(window, (255, 0, 0), self.array[0], 2)

        self.array[1] = (self.x + 35, self.y + 5, self.width - 70, self.height - 45)
        # pygame.draw.rect(window, (255, 0, 0), self.array[1], 2)

        self.array[2] = (self.x + 33, self.y + 40, self.width - 88, self.height - 40)
        # pygame.draw.rect(window, (255, 0, 0), self.array[2], 2)

        window.blit(pygame.transform.scale(self.img, (self.width, self.height)), (self.x, self.y))

    def collide(self, character):
        for i in range(0, 3):
            if not (((self.array[i][1] > character.hitbox[1] + character.hitbox[3]) or (
                    character.hitbox[1] > self.array[i][1] + self.array[i][3]))
                    or ((self.array[i][0] > character.hitbox[0] + character.hitbox[2]) or (
                            character.hitbox[0] > self.array[i][0] + self.array[i][2]))):
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
        self.array = [self.hitbox, self.hitbox, self.hitbox, self.hitbox]
        self.img = pygame.image.load(os.path.join('../resources/obstacles', 'rider.png'))

    def draw(self, window):
        self.array[0] = (self.x - 5, self.y + 50, self.width - 20, self.height - 50)
        # pygame.draw.rect(window, (255, 0, 0), self.array[0], 2)

        self.array[1] = (self.x + 47, self.y + 12, self.width - 48, self.height - 50)
        # pygame.draw.rect(window, (255, 0, 0), self.array[1], 2)

        self.array[2] = (self.x + 23, self.y + 90, self.width - 100, self.height - 150)
        # pygame.draw.rect(window, (255, 0, 0), self.array[2], 2)

        self.array[3] = (self.x + 70, self.y + 80, self.width - 190, self.height - 170)
        # pygame.draw.rect(window, (255, 0, 0), self.array[3], 2)

        window.blit(pygame.transform.scale(self.img, (self.width, self.height)), (self.x, self.y))

    def collide(self, character):
        for i in range(0, 4):
            if not (((self.array[i][1] > character.hitbox[1] + character.hitbox[3]) or (
                    character.hitbox[1] > self.array[i][1] + self.array[i][3]))
                    or ((self.array[i][0] > character.hitbox[0] + character.hitbox[2]) or (
                            character.hitbox[0] > self.array[i][0] + self.array[i][2]))):
                return True
        return False
