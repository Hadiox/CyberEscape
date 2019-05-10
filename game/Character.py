import pygame
import os


class Character(object):
    run = [pygame.image.load(os.path.join('resources/character/run', 'run-' + str(x) + '.png')) for x in
           range(1, 8)]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.run_counter = 0
        self.speed = 8
        self.hitbox = (width,height)

    def display(self, win):
        if self.run_counter >= 7 * self.speed:
            self.run_counter = 0
        win.blit(pygame.transform.scale(self.run[self.run_counter // self.speed], (100, 100)), (self.x, self.y))
        self.run_counter += 1
