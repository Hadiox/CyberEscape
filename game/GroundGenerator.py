import threading
import time
from CyberEscape.game.Ground import *
from CyberEscape.game.Obstacles import *
import random


class GroundGenerator(threading.Thread):
    def __init__(self, objects, screen_height):
        threading.Thread.__init__(self)
        self.objects = objects
        self.screen_height = screen_height
        self.obstacle = 0

    def run(self):
        while (True):
            if self.obstacle == 1:
                obs_height = random.randrange(50, 200)
                obs_width = random.randrange(50, 200)
                self.objects.append(Rectangle(self.screen_height + 20, 598 - obs_height, obs_width,
                                              obs_height))
                self.obstacle = 0
            if self.obstacle == 2:
                obs_height = random.randrange(50, 200)
                obs_width = random.randrange(200,300)
                self.objects.append(Truck(self.screen_height + 20, 598 - obs_height, obs_width,
                                              obs_height))
                self.obstacle = 0

            self.objects.append(Ground(self.screen_height + 20, 598, 400, 180))
            time.sleep(0.500)
