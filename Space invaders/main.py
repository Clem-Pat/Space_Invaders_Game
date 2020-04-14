from pygame import *
import pygame.gfxdraw
import random
import time

from characters.invader import Invader as Invader
from characters.invader import Master_Invader as Master_Invader
from characters.player import Player as Player
from characters.projectile import Projectile as Projectile

from map import create_map as map

def create_fonts():
    L = []
    L.append(font.Font("Fonts/Arial.ttf", 20))
    L.append(font.Font("Fonts/GROBOLD.ttf", 30))
    L.append(font.Font("Fonts/GROBOLD.ttf", 40))

    return L


def create_texts(fonts, couleurs):
    L={}
    L['label_lives'] = fonts[0].render("Lives :", 1, couleurs[1])
    L['label_finish'] = fonts[1].render("CONGRATULATIONS", 1, couleurs[1])
    L['label_game_over'] = fonts[2].render("GAME OVER", 1, couleurs[1])
    L['label_enter_revive'] = fonts[1].render("Press Enter to revive", 1, couleurs[2])
    L['label_enter_restart'] = fonts[1].render("Press Enter to restart", 1, couleurs[2])
    return L


def get_events(app, running, game_over, cheat_mode, nbr_vies, player, L_invaders, L_friendly_projectiles):


    cheat = cheat_mode
    over = game_over
    run = running
    vies = nbr_vies
    again = False

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

                        player.direction = 'right'
                        player.direction_wanted = 'right'

                        L_invaders = create_invaders()
                        for i in L_invaders:
                            place_object(app, i)

                        player.x = player.initial_x
                        place_object(app, player)

                        vies -= 1
                        again = False

                    else:
                        run = False
                        again = True

                elif over == 'gagne':
                    run = False
                    again = True

    return run, cheat, over, vies, again, player, L_friendly_projectiles


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


def finish(app, game_over, nbr_vies, player, label_finish, label_game_over, label_enter_revive, label_enter_restart):

    if game_over == 'gagne':

        place_object(app, player)

        app.blit(label_finish, (292, 220))
        app.blit(label_enter_restart, (292,345))

    elif game_over == 'perdu':

        place_object(app, player)

        app.blit(label_game_over, (320,210))
        if nbr_vies != 0:
            app.blit(label_enter_revive, (298,345))
        else:
            app.blit(label_enter_restart, (292,345))

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
    L_ennemy_projectiles.append(Projectile(200,100,"ennemy"))

    player_vie1 = Player(60, 100)
    player_vie2 = Player(100, 100)
    player_vie3 = Player(140, 100)
    nbr_vies = 2

    turn = False
    cheat_mode = False
    game_over = False
    running = True
    n_boucle = 0
    while running == True:
        n_boucle += 1
        temps = time.time() - time_start
        app.fill((0, 0, 0))
        map(app)

        ### Events : ###
        running, cheat_mode, game_over, nbr_vies, play_again, player, L_friendly_projectiles = get_events(app, running, game_over, cheat_mode, nbr_vies, player, L_invaders, L_friendly_projectiles)

        game_over = test_collision(app, player, L_invaders, L_ennemy_projectiles, L_friendly_projectiles, game_over)


        if game_over == False :
            ### game not finished ###
            player.player_move(app)

            for i in L_invaders:
                game_over = i.invader_move(app)


            for p in range(len(L_friendly_projectiles)):
                try:
                    L_friendly_projectiles[p].projectile_move(app, n_boucle)
                    if L_friendly_projectiles[p].y <= 90:
                        L_friendly_projectiles.pop(p)
                except: pass

            for q in range(len(L_ennemy_projectiles)):
                try:
                    L_ennemy_projectiles[q].projectile_move(app, n_boucle)
                    if L_ennemy_projectiles[q].y >= 500:
                        L_ennemy_projectiles.pop(q)
                except :pass


        if game_over != False:
            finish(app, game_over, nbr_vies, player, text['label_finish'], text['label_game_over'], text['label_enter_revive'], text['label_enter_restart'])


        app.blit(text['label_lives'], (50, 50))
        app.blit(player_vie1.img, player_vie1.rect)  # l'objet et son rectangle
        if nbr_vies >= 1:
            app.blit(player_vie2.img, player_vie2.rect)  # l'objet et son rectangle
            if nbr_vies >= 2:
                app.blit(player_vie3.img, player_vie3.rect)  # l'objet et son rectangle


        display.update()

        player.old_direction = player.direction
        for i in L_invaders :
            i.old_direction = i.direction

        time.sleep(0.0015)

    quit()

    if play_again == True:
        main()


if __name__ == '__main__':
    main()
