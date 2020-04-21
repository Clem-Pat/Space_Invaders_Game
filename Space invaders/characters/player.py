"""player"""

from pygame import *
import pygame.gfxdraw
import random
import time

from characters.projectile import Projectile as Projectile
import os
player_path = os.path.dirname(os.path.abspath(__file__))
if player_path.endswith('characters'):
    player_path = player_path[:-10]

class Player():
    def __init__(self, x, y):
        self.initial_x = x
        self.initial_y = y
        self.x = x
        self.y = y
        self.direction_wanted = 'right'
        self.direction = "right"
        self.img = image.load(player_path+"\\images\\player.jpg")
        self.img = self.img.convert()
        self.rect = self.img.get_rect()
        self.rect.center = (self.x, self.y)
        self.img.set_colorkey((0, 0, 0))

        self.hauteur = 25
        self.largeur = 30


    def player_move(self,app):

        if self.x >= 694 - int(self.largeur/2) and self.direction_wanted == 'right':
            pass
        elif self.x <= 197 + int(self.largeur/2) and self.direction_wanted == 'left':
            pass
        else:
            self.direction = self.direction_wanted
            if self.direction == 'right' :
                self.x += 1
            elif self.direction == 'left' :
                self.x -= 1

        self.old_direction = self.direction

        self.rect.center = (self.x, self.y)


    def player_shoot(self,L_friendly_projectiles):
        L_friendly_projectiles.append(Projectile(self.x,self.y,"friendly"))
