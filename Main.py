import pygame
import os
from PIL import Image
import ctypes


def set_screen_prop():
    user32 = ctypes.windll.user32
    screen_size = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    size = screen_size
    pygame.display.set_caption("Window")
    return pygame.display.set_mode(size, pygame.FULLSCREEN)


pygame.init()
usr32 = ctypes.windll.user32
screen_width = usr32.GetSystemMetrics(1)
screen_height = usr32.GetSystemMetrics(0)
game_window = set_screen_prop()
if len(os.listdir('resources/background_fit')) == 0:
    for x in range(0, 60):
        img = Image.open('resources/background/frame_' + str(x) + '_delay-0.03s.gif')
        img = img.resize((screen_height, screen_width), Image.ANTIALIAS)
        img.save('resources/background_fit/frame_' + str(x) + '_delay-0.03s.gif')
background = [pygame.image.load(os.path.join('resources/background_fit', 'frame_' + str(x) + '_delay-0.03s.gif'))
              for x in range(0, 60)]
bg_1_x = 0
clock = pygame.time.Clock()


class Character(object):
    run = [pygame.image.load(os.path.join('resources/character/run', 'run-' + str(x) + '.png')) for x in range(1, 8)]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.run_counter = 0

    def display(self, win):
        if self.run_counter > 42:
            self.run_counter = 0
        win.blit(self.run[self.run_counter // 6], (self.x, self.y))
        self.run_counter += 1


def redraw_background(frame, bg_speed):
    game_window.blit(background[frame // bg_speed], (bg_1_x, 0))
    pygame.display.update()


speed = 60
run = True
frame_counter = 0
bg_speed = 2
while run:
    redraw_background(frame_counter, bg_speed)
    frame_counter += 1
    if frame_counter == 60 * bg_speed:
        frame_counter = 0
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True
            pygame.quit()
            quit()
