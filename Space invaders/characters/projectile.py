"""projectile"""

from pygame import *
import pygame.gfxdraw
import random
import time

import os
projectile_path = os.path.dirname(os.path.abspath(__file__))
if projectile_path.endswith('characters'):
    projectile_path = projectile_path[:-10]


class Projectile():
    def __init__(self, x, y, nature):
        self.initial_x = x
        self.initial_y = y
        self.x = x
        self.y = y

        if nature == 'ennemy':
            self.direction = "down"
            self.speed = 3
        elif nature == 'friendly':
            self.direction = "up"
            self.speed = 1
        else:
            print("ERREUR DE FRAPPE ennemy OU friendly")

        self.img = image.load(projectile_path+"\\images\\projectile {}.png".format(nature)) #ennemy ou friendly
        self.img = self.img.convert()
        self.rect = self.img.get_rect()
        self.rect.center = (self.x, self.y)
        self.img.set_colorkey((0, 0, 0))

        self.hauteur = 40
        if nature == "ennemy" :
            self.largeur = 3
        elif nature == "friendly":
            self.largeur = 2


    def projectile_move(self,app,n_boucle):

        if self.direction == 'up':
            self.y -= 1
            if n_boucle%7 == 0:
                self.img = transform.flip(self.img, True, True)
        elif self.direction == 'down':
            self.y += 1
            if n_boucle%7 == 0:
                self.img = transform.flip(self.img, True, True)

        self.rect.center = (self.x, self.y)
