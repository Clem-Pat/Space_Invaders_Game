from pygame import *
import pygame.gfxdraw
import random
import time
import math

from characters.invader import Invader as Invader
from characters.invader import Master_Invader as Master_Invader
from characters.player import Player as Player
from characters.projectile import Projectile as Projectile

from map import create_map as map

import os
path = os.path.dirname(os.path.abspath(__file__))


def create_fonts():
    L = []
    L.append(font.Font(path+"\\Fonts\\Arial.ttf", 20))
    L.append(font.Font(path+"\\Fonts\\GROBOLD.ttf", 30))
    L.append(font.Font(path+"\\Fonts\\GROBOLD.ttf", 40))

    return L


def create_texts(fonts, couleurs):
    L={}
    L['label_lives'] = fonts[0].render("Lives :", 1, couleurs[1])
    L['label_finish'] = fonts[1].render("CONGRATULATIONS", 1, couleurs[1])
    L['label_game_over'] = fonts[2].render("GAME OVER", 1, couleurs[1])
    L['label_enter_revive'] = fonts[1].render("Press Enter to revive", 1, couleurs[2])
    L['label_enter_restart'] = fonts[1].render("Press Enter to restart", 1, couleurs[2])
    return L


def create_invaders():
    L = []
    for i in range(17):
        L.append(Invader(250+25*i,100,1))
    for j in range(12):
        L.append(Invader(250+35*j,150,2))
    for k in range(12):
        L.append(Invader(260+35*k,200,3))
    for i in range(17):
        L.append(Invader(250+25*i,250,1))
    return L


def place_object(app, object):
    object.rect.center = (object.x, object.y)
    app.blit(object.img, object.rect)


def test_collision(surface, player, L_invaders, L_ennemy_projectiles, L_friendly_projectiles, game_over):

    over = False

    for i in L_ennemy_projectiles:
        if i.rect.colliderect(player.rect):
            over = 'perdu'

    L_i_a_effacer = []
    L_j_a_effacer = []
    for i in L_friendly_projectiles:
        for j in L_invaders:
            if i.rect.colliderect(j.rect):
                L_i_a_effacer.append(L_friendly_projectiles.index(i))
                L_j_a_effacer.append(L_invaders.index(j))


    for i in L_i_a_effacer:
        if L_friendly_projectiles != []:
            try: L_friendly_projectiles.pop(i)
            except: pass

    for j in L_j_a_effacer:
        if L_invaders != []:
            try: L_invaders.pop(j)
            except : pass


    if L_invaders == []:
        over = 'gagne'


    return over


def get_events(app, running, game_over, cheat_mode, nbr_vies, player, L_invaders, L_friendly_projectiles, L_game_over):


    cheat = cheat_mode
    over = game_over
    run = running
    vies = nbr_vies

    for evt in event.get():
        if evt.type == QUIT:
            run = False
        if evt.type == KEYDOWN:
            if evt.key == K_ESCAPE or evt.key == K_DELETE:
                run = False

            # cheat codes :
            elif evt.key == K_c:
                rect_surface = Surface((10,10))
                rect_surface.fill((255,0,0))
                rect = rect_surface.get_rect()
                rect.center = (760,0)
                app.blit(rect_surface,rect)
                display.flip()
                time.sleep(0.2)
                for evt in event.get():
                    if evt.type == KEYDOWN:
                        if evt.key == K_o:
                            rect_surface = Surface((10,10))
                            rect_surface.fill((0,255,0))
                            rect = rect_surface.get_rect()
                            rect.center = (760,0)
                            app.blit(rect_surface,rect)
                            display.flip()
                            time.sleep(0.2)
                            for evt in event.get():
                                if evt.type == KEYDOWN:
                                    if evt.key == K_e:
                                        rect_surface = Surface((10,10))
                                        rect_surface.fill((0,0,255))
                                        rect = rect_surface.get_rect()
                                        rect.center = (760,0)
                                        app.blit(rect_surface,rect)
                                        display.flip()
                                        time.sleep(0.2)
                                        for evt in event.get():
                                            if evt.type == KEYDOWN:
                                                if evt.key == K_u:
                                                    rect_surface = Surface((10,10))
                                                    rect_surface.fill((255,255,0))
                                                    rect = rect_surface.get_rect()
                                                    rect.center = (760,0)
                                                    app.blit(rect_surface,rect)
                                                    display.flip()
                                                    time.sleep(0.2)
                                                    for evt in event.get():
                                                        if evt.type == KEYDOWN:
                                                            if evt.key == K_r:
                                                                rect_surface = Surface((10,10))
                                                                rect_surface.fill((0,255,255))
                                                                rect = rect_surface.get_rect()
                                                                rect.center = (760,0)
                                                                app.blit(rect_surface,rect)
                                                                display.flip()
                                                                cheat = True

            elif evt.key == K_RIGHT:
                player.direction_wanted = 'right'
            elif evt.key == K_LEFT:
                player.direction_wanted = 'left'
            elif evt.key == K_SPACE:
                player.player_shoot(L_friendly_projectiles)

            elif evt.key == K_RETURN:
                if over == 'perdu':
                    if vies != 0:
                        app.fill((0, 0, 0))

                        player.direction = 'right'
                        player.direction_wanted = 'right'

                        L_invaders = create_invaders()
                        for i in L_invaders:
                            place_object(app, i)

                        player.x = player.initial_x
                        place_object(app, player)

                        vies -= 1
                        run = True
                        over = False
                        L_game_over = []

                    else:
                        run = False
                        main()

                elif over == 'gagne':
                    run = False
                    main()

    return run, over, cheat, vies, player, L_friendly_projectiles, L_invaders, L_game_over


def finish(app, game_over, nbr_vies, player, label_finish, label_game_over, label_enter_revive, label_enter_restart):

    if game_over == 'gagne':
        try:
            place_object(app, player)
        except: pass

        try:
            app.blit(label_finish, (292, 220))
            app.blit(label_enter_restart, (292,345))
        except : pass

    elif game_over == 'perdu':
        try:
            place_object(app, player)
        except: pass

        try:
            app.blit(label_game_over, (320,210))
            if nbr_vies != 0:
                app.blit(label_enter_revive, (298,345))
            else:
                app.blit(label_enter_restart, (292,345))
        except: pass


def attack_player(L_invaders, player, L_ennemy_projectiles, n_boucle):
    if n_boucle % 300 == 0:
        L_distances = []
        for i in L_invaders:
            L_distances.append(math.sqrt((i.x - player.x)**2 + (i.y - player.y)**2))
        attaquant = L_invaders[L_distances.index(min(L_distances))]
        attaquant.invader_shoot(L_ennemy_projectiles)

    if n_boucle % 900 == 0:
        L_distances = []
        for i in L_invaders:
            x_recherche = (i.y - player.y) * (i.speed/player.speed) + player.x
            L_distances.append(math.sqrt((i.x - x_recherche)**2))
        attaquant = L_invaders[L_distances.index(min(L_distances))]
        attaquant.invader_shoot(L_ennemy_projectiles)


def main():
    global app, temps, time_start

    # chdir("C:/Users/cleme/Desktop/Documents/1. DOCUMENTS CLEMENT/TRAVAIL/Post BAC/projets personnels info/MINI JEUX/Pacman/pacman_game")
    fps = 30

    clock = pygame.time.Clock()  # pour fps
    init()
    app = display.set_mode((800, 550))
    display.set_caption('SPACE INVADERS')
    couleurs = [(0, 255, 0), (255, 255, 255), (255,255,0)]  # vert, blanc, jaune

    temps = 0
    delta_ms = clock.tick(fps)
    delta_s = delta_ms / 1000

    fonts = create_fonts()
    text = create_texts(fonts, couleurs)

    time_start = time.time()

    player = Player(445, 490)
    L_invaders = create_invaders()
    L_ennemy_projectiles = []
    L_friendly_projectiles = []

    player_vie1 = Player(60, 100)
    player_vie2 = Player(100, 100)
    player_vie3 = Player(140, 100)
    nbr_vies = 0

    temps_de_boucle = 0.0015
    turn = False
    cheat_mode = False
    game_over = False
    running = True
    n_boucle = 0
    L_game_over = []
    while running == True:
        n_boucle += 1
        temps = time.time() - time_start
        app.fill((0, 0, 0))
        map(app)

        ### Events : ###
        running, test_over, cheat_mode, nbr_vies, player, L_friendly_projectiles, L_invaders, L_game_over = get_events(app, running, game_over, cheat_mode, nbr_vies, player, L_invaders, L_friendly_projectiles, L_game_over)
        L_game_over.append(test_over)

        test_over = test_collision(app, player, L_invaders, L_ennemy_projectiles, L_friendly_projectiles, game_over)
        L_game_over.append(test_over)

        if 'perdu' not in L_game_over and 'gagne' not in L_game_over :
            ### game not finished ###
            if n_boucle % 1 == 0:
                player.player_move(app)


            """deplacer les invaders à une vitesse 6 fois moins élevée que player"""
            try:
                if n_boucle % L_invaders[0].speed == 0:
                    L_end_of_line = []
                    L_game_over = []  #on réinitialise la liste des tests de fin de jeu
                    for i in L_invaders:
                        test_over, end_of_line = i.invader_move(app)
                        L_end_of_line.append(end_of_line)
                        L_game_over.append(test_over)

                    if True in L_end_of_line: #Si un invader arrive au bout de la ligne, tous descendent d'un cran
                        for i in L_invaders:
                            i.y += 25
                            i.invader_change_direction()
            except: pass

            if n_boucle % 300 == 0:
                if cheat_mode == False:
                    attack_player(L_invaders, player, L_ennemy_projectiles, n_boucle)


            """deplacer les projectiles"""
            try:
                if n_boucle % L_friendly_projectiles[0].speed ==0:
                    for p in range(len(L_friendly_projectiles)):
                        try:
                            L_friendly_projectiles[p].projectile_move(app, n_boucle)
                            if L_friendly_projectiles[p].y <= 90:
                                L_friendly_projectiles.pop(p)
                        except: pass
            except: pass

            try:
                if n_boucle % L_ennemy_projectiles[0].speed == 0:
                    for q in range(len(L_ennemy_projectiles)):
                        try:
                            L_ennemy_projectiles[q].projectile_move(app, n_boucle)
                            if L_ennemy_projectiles[q].y >= 500:
                                L_ennemy_projectiles.pop(q)
                        except :pass
            except: pass

            """afficher les objets (player, invaders, projectiles)"""
            player.old_direction = player.direction
            app.blit(player.img, player.rect)

            for i in L_invaders :
                app.blit(i.img, i.rect)
                i.old_direction = i.direction
            for p in L_friendly_projectiles:
                app.blit(p.img, p.rect)
            for q in L_ennemy_projectiles:
                app.blit(q.img, q.rect)


        finish(app, game_over, nbr_vies, player, text['label_finish'], text['label_game_over'], text['label_enter_revive'], text['label_enter_restart'])


        if 'perdu' in L_game_over:
            game_over = 'perdu'
        elif 'gagne' in L_game_over:
            game_over = 'gagne'


        """afficher le nb de vies"""
        try:
            app.blit(text['label_lives'], (50, 50))
            app.blit(player_vie1.img, player_vie1.rect)  # l'objet et son rectangle
            if nbr_vies >= 1:
                app.blit(player_vie2.img, player_vie2.rect)  # l'objet et son rectangle
                if nbr_vies >= 2:
                    app.blit(player_vie3.img, player_vie3.rect)  # l'objet et son rectangle
            display.update()
        except: pass

        if cheat_mode == True:
            for i in L_invaders:
                i.speed = 100
        


        time.sleep(temps_de_boucle)

    quit()


if __name__ == '__main__':
    main()
