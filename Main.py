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
    run = [pygame.image.load(os.path.join('resources/character/run', 'run-' + str(x) + '.png')) for x in
           range(1, 8)]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.run_counter = 0
        self.speed = 8

    def display(self, win):
        if self.run_counter >= 7 * self.speed:
            self.run_counter = 0
        win.blit(pygame.transform.scale(self.run[self.run_counter // self.speed], (100, 100)), (self.x, self.y))
        self.run_counter += 1


def redraw_background(frame, bg_speed):
    game_window.blit(background[frame // bg_speed], (bg_1_x, 0))
    for obj in objects:
        obj.draw(game_window)


speed = 60
objects = []
run = True
frame_counter = 0
pygame.time.set_timer(pygame.USEREVENT + 1, 120000)
flag = 0
bg_speed = 10
pygame.time.set_timer(pygame.USEREVENT + 2,200)
runner = Character(200, 500, 27, 27)


class Ground(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (x, y, width, height)
        self.img = pygame.image.load(os.path.join('resources/Ground', 'simple_ground.png'))

    def draw(self, window):
        self.hitbox=(self.x+25,self.y+3,self.width,self.height)
        window.blit(pygame.transform.scale(self.img, (self.width, self.height)), (self.x, self.y))
        #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)


def draw_runner():
    runner.display(game_window)


def draw_init_objects():
    for i in range (0,13):
        objects.append(Ground(i*122-50,598,180,180))


draw_init_objects()
while run:
    redraw_background(frame_counter, bg_speed)
    for obj in objects:
        obj.x -= 10
        if obj.x < obj.width * (-1):
            objects.pop(objects.index(obj))
    draw_runner()
    pygame.display.update()
    frame_counter += 1
    if frame_counter == 60 * bg_speed:
        frame_counter = 0
        if flag == 1 and bg_speed > 1:
            bg_speed -= 1
            flag = 0
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True
            pygame.quit()
            quit()
        if event.type == pygame.USEREVENT + 2:
            objects.append(Ground(screen_height + 20, 598, 180, 180))
        if event.type == pygame.USEREVENT + 1:
            flag = 1
