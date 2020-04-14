"""invader"""
"""lignes initiales de déplacement : 100, 150, 200, 250, 300"""
"""lignes de déplacement : 100, 125, 150, 175, 200, 225, 250, 275, 300"""

from pygame import *
import pygame.gfxdraw
import random
import time

class Invader():
    def __init__(self, x, y, nature):
        self.initial_x = x
        self.initial_y = y
        self.x = x
        self.y = y
        self.direction_wanted = 'right'
        self.direction = "right"
        self.img = image.load("images/invader {}.jpg".format(nature))
        self.img = self.img.convert()
        self.rect = self.img.get_rect()
        self.rect.center = (self.x, self.y)
        self.img.set_colorkey((0, 0, 0))

        if nature == 1:
            self.hauteur = 20
            self.largeur = 20
        else:
            self.hauteur = 20
            self.largeur = 30

    def invader_move(self,app):

        self.direction = self.direction_wanted
        if self.direction == 'right':
            self.x += 1
        elif self.direction == 'left':
            self.x -= 1


        if self.x >= 694 - int(self.largeur/2) or self.x <= 197 + int(self.largeur/2):
            self.y += 25
            if self.direction == 'right':
                self.direction_wanted = 'left'
            elif self.direction == 'left':
                self.direction_wanted = 'right'

        self.rect.center = (self.x, self.y)
        app.blit(self.img, self.rect)

        if self.y > 450:
            game_over = 'perdu'
        else:
            game_over = False
        return game_over


class Master_Invader():
    def __init__(self, x, y):
        self.initial_x = x
        self.initial_y = y
        self.x = x
        self.y = y
        self.direction_wanted = 'right'
        self.direction = "right"
        self.img = image.load("images/master_invader.jpg")
        self.img = self.img.convert()
        self.rect = self.img.get_rect()
        self.rect.center = (self.x, self.y)
        self.img.set_colorkey((0, 0, 0))
