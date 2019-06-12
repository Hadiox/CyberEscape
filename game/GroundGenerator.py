import threading
import time
from game.Ground import *
from game.Obstacles import *
import random


class GroundGenerator(threading.Thread):
    def __init__(self, objects, screen_height):
        threading.Thread.__init__(self)
        self.objects = objects
        self.screen_height = screen_height
        self.obstacle = 0
        self.stopped = False

    def run(self):
        while not self.stopped:
            if self.obstacle == 1:
                obs_height = 75
                obs_width = 75
                self.objects.append(Rectangle(self.screen_height + 20, 598 - obs_height, obs_width,
                                              obs_height))
                self.objects.append(Rectangle(self.screen_height + 30, 524 - obs_height, obs_width,
                                              obs_height))
                self.objects.append(Rectangle(self.screen_height + 45, 598 - obs_height, obs_width,
                                              obs_height))
                self.objects.append(Rectangle(self.screen_height + 75, 524 - obs_height, obs_width,
                                              obs_height))
                self.objects.append(Rectangle(self.screen_height + 75, 598 - obs_height, obs_width,
                                              obs_height))

                self.obstacle = 0

            if self.obstacle == 2:
                obs_height = 200
                obs_width = 350
                self.objects.append(Truck(self.screen_height + 20, 598 - obs_height, obs_width,
                                              obs_height))
                self.obstacle = 0

            if self.obstacle == 3:
                obs_height = 100
                obs_width = 250
                self.objects.append(Police(self.screen_height + 20, 598 - obs_height, obs_width,
                                          obs_height))
                self.obstacle = 0

            if self.obstacle == 4:
                obs_height = 75
                obs_width = 100
                self.objects.append(Drone(self.screen_height + 20, 528 - obs_height, obs_width,
                                          obs_height))
                self.objects.append(Drone(self.screen_height + 30, 438 - obs_height, obs_width,
                                          obs_height))
                self.objects.append(Drone(self.screen_height + 40, 348 - obs_height, obs_width,
                                          obs_height))

                self.obstacle = 0

            if self.obstacle == 5:
                obs_height = 90
                obs_width = 200
                self.objects.append(Rider(self.screen_height + 20, 598 - obs_height, obs_width,
                                          obs_height))
                self.obstacle = 0

            if self.obstacle == 6:
                obs_height = 75
                obs_width = 100
                self.objects.append(Drone(self.screen_height + 20, 375 - obs_height, obs_width,
                                          obs_height))
                self.objects.append(Drone(self.screen_height + 100, 460 - obs_height, obs_width,
                                          obs_height))
                self.objects.append(Drone(self.screen_height + 180, 375  - obs_height, obs_width,
                                          obs_height))
                self.objects.append(Drone(self.screen_height + 260, 460 - obs_height, obs_width,
                                          obs_height))
                self.objects.append(Drone(self.screen_height + 340, 375 - obs_height, obs_width,
                                          obs_height))
                self.objects.append(Drone(self.screen_height + 420, 460 - obs_height, obs_width,
                                          obs_height))
                self.objects.append(Drone(self.screen_height + 500, 375 - obs_height, obs_width,
                                          obs_height))
                self.objects.append(Drone(self.screen_height + 580, 460 - obs_height, obs_width,
                                          obs_height))
                self.obstacle = 0



            self.objects.append(Ground(self.screen_height + 20, 598, 400, 180))
            time.sleep(0.500)

    def stop(self):
        self.stopped = True
