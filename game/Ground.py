import pygame
import os


class Ground(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.id = 0
        self.height = height
        self.hitbox = (x, y, width, height)
        self.img = pygame.image.load(os.path.join('../resources/Ground', 'simple_ground.jpg'))

    def draw(self, window):
        self.hitbox = (self.x + 25, self.y + 3, self.width, self.height)
        window.blit(pygame.transform.scale(self.img, (self.width, self.height)), (self.x, self.y))
        # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
