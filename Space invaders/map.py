from pygame import *
import pygame.gfxdraw
import random
import time

def create_map(app):
    pygame.gfxdraw.hline(app, 196, 694, 70, (255,255,255))  # mur du haut
    pygame.gfxdraw.vline(app, 196, 70, 520, (255,255,255))  # mur de gauche
    pygame.gfxdraw.hline(app, 196, 694, 520, (255,255,255))  # mur du bas
    pygame.gfxdraw.vline(app, 694, 70, 520, (255,255,255))  # mur de droite
