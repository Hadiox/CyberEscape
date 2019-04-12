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


class Ground(object):

    ground = pygame.image.load(os.path.join('resources/ground/ground.png'))

    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height

    def display(self,win):
        win.blit(pygame.transform.scale(self.ground,(self.width,self.height)), (self.x, self.y))


class Character(object):
    run = [pygame.image.load(os.path.join('resources/character/run', 'run-' + str(x) + '.png')) for x in range(1, 8)]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.run_counter = 0

    def display(self, win):
        if self.run_counter >=48:
            self.run_counter = 0
        win.blit(pygame.transform.scale(self.run[self.run_counter // 7],(self.width,self.height)), (self.x, self.y))
        self.run_counter += 1


def redraw_background(frame, bg_speed):
    game_window.blit(background[frame // bg_speed], (bg_1_x, 0))
    for obj in objects:
        obj.display(game_window)

def draw_init_objects():
    for i in range(0,13):
        objects.append(Ground(i*120,598,180,180))

speed = 60
runner = Character(200,500,100,100)
pygame.time.set_timer(pygame.USEREVENT+1,120000)
pygame.time.set_timer(pygame.USEREVENT+2,200)
flag = 0
run = True
frame_counter = 0
objects = []
bg_speed = 10
draw_init_objects()
while run:
    redraw_background(frame_counter, bg_speed)
    for obj in objects:
        obj.x-=10
        if(obj.x<obj.width*(-1)):
            objects.pop(objects.index(obj))
    runner.display(game_window)
    pygame.display.update()
    frame_counter += 1
    if frame_counter == 60 * bg_speed:
        frame_counter = 0
        if flag==1:
            bg_speed-=1
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True
            pygame.quit()
            quit()
        if event.type == pygame.USEREVENT+1:
            flag = 1
        if event.type == pygame.USEREVENT+2:
            objects.append(Ground(screen_height+20,598,180,180))
