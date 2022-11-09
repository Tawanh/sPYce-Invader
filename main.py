# Créé par Nathan.zorroche, le 13/10/2022 en Python 3.7

#from joueur import Joueur
import pygame
from pygame.locals import *
import sys
from time import sleep


from joueur import Joueur
from projectile import Projectile
from boss import Boss
from ennemi import Liste_ennemi
from shield import Shield


#init fenetre pygame
pygame.init()
clock = pygame.time.Clock()
FPS = 60
longueur = 1080
largeur = 800
screen = pygame.display.set_mode((longueur, largeur))
font = pygame.font.Font("font/CosmicAlien-V4Ax.ttf", 50)

#variable ennemi
paterne_ennemi_horizontal = True
direction = [1,0]
vitesse = 0.3
longueur_deplacement_vertical = 20
longueur_deplacement_horizontal = 100

liste_ennemi = Liste_ennemi(15,4,20,40,"images/invader.png",11*4,8*4,(longueur,largeur),longueur_deplacement_horizontal)
compteur = 0

#variable bouclier
liste_tout_shield = []
for i in range(4):
    liste_tout_shield.append(Shield((100 + i * 250,500) , 30, "images/bouclier.png","images/boucliergauche.png","images/bouclierdroit.png"))
joueur = Joueur(screen)
boss = Boss(screen)

boss_kill = False
compt = 0
running = True
delai_tir_joueur = 0
projectiles_joueur = []
projectiles_ennemis = []
etat = "alive"

while running:

    if etat == "alive":  
        etat = joueur.etat
        screen.fill([0,0,0])
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.type == pygame.QUIT:
                    running = False
                if event.key == pygame.K_SPACE and delai_tir_joueur <= 0:
                    projectiles_joueur.append(Projectile(2 ,(joueur.getCoords(16)),-1, screen))
                    if joueur._score >= 200:
                        delai_tir_joueur = 30
                    else:
                        delai_tir_joueur = 60
                        

        joueur.moov(longueur)

        #fixer le nombre de fps sur ma clock
        clock.tick(FPS)

        #Detecte les collisons des balles
        if projectiles_joueur != []:
            for i , e in enumerate(projectiles_joueur):
                if e.is_collide(largeur):
                    del e
                elif not  boss_kill and e.rect.colliderect(boss.getRect()) and joueur._score >= 200:
                    projectiles_joueur.pop(i)
                    boss._pv -= 1
                    if boss._pv ==0:
                        boss.kill()
                        boss_kill = True
                elif e.is_collide(largeur, liste_ennemi.getlistennemi()):
                    joueur.ajout_score()
                    projectiles_joueur.pop(i)
                elif e.is_collide(largeur, liste_tout_shield, True, "haut"):
                    projectiles_joueur.pop(i)
                else:
                    e.afficher()
        if projectiles_ennemis != []:
            for i, e in enumerate(projectiles_ennemis):
                if e.is_collide(largeur, joueur):
                    projectiles_ennemis.pop(i)
                elif e.is_collide(largeur, liste_tout_shield, True, "bas"):
                    projectiles_ennemis.pop(i)
                else:
                    e.afficher()

        #movement ennemis
        compteur +=1
        if paterne_ennemi_horizontal:
            liste_ennemi.movement_all_ennemi(vitesse,direction,screen,500,projectiles_ennemis)
            if compteur == longueur_deplacement_horizontal//vitesse:
                paterne_ennemi_horizontal = False
                compteur = 0
        else:
            liste_ennemi.movement_all_ennemi(vitesse,[0,1],screen,500,projectiles_ennemis)
            if compteur == longueur_deplacement_vertical//vitesse:
                paterne_ennemi_horizontal = True
                direction[0] *= -1
                compteur = 0
        delai_tir_joueur -=1
        
        joueur.afficher()
        

        #bouclier
        for i in liste_tout_shield:
            i.afficher(screen)

        #score
        score_texte = font.render(f"Score : {joueur._score}", 1, (255,255,255))
        screen.blit(score_texte, (380, 700))

        #vie
        joueur.affiche_vie()
        
        #Apparition du boss
        if joueur._score == 200:
            liste_ennemi._liste_ennemi = []
            if not boss_kill:
                boss.afficher()
                boss.movement(longueur, projectiles_ennemis)
            else:
                etat = "win"
        
    
    #Changement de phase de jeux, lose or win

    elif etat == "dead":
            screen.fill([0,0,0])
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.type == pygame.QUIT:
                        running = False
            font = pygame.font.Font('font/game_over.ttf', 128)
            texte_game_over = font.render('Oh non tu as perdu... ', True, (255,0,0))
            texte_encouragement = font.render('Tu feras mieux la prochaine fois', True, (255,255,255))
            texte_quitter = font.render('Appuie sur \'echap\' quitter', True, (128,128,128))
            screen.blit(texte_game_over, (screen.get_width()//2 - texte_game_over.get_width()//2,screen.get_height()//2 - texte_game_over.get_height()//2-100))
            screen.blit(texte_encouragement, (screen.get_width()//2 - texte_encouragement.get_width()//2,screen.get_height()//2 - texte_encouragement.get_height()//2))
            screen.blit(texte_quitter, (screen.get_width()//2 - texte_quitter.get_width()//2,screen.get_height()//2 - texte_quitter.get_height()//2+100))
    elif etat == "win":
            screen.fill([0,0,0])
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.type == pygame.QUIT:
                        running = False
            font = pygame.font.Font('font/game_over.ttf', 128)
            texte_game_over = font.render('Bravo, tu as gagné contre le boss !', True, (0,255,0))
            texte_quitter = font.render('Appuie sur la touche \'echap\' pour quitter ', True, (128,128,128))
            screen.blit(texte_game_over, (screen.get_width()//2 - texte_game_over.get_width()//2,screen.get_height()//2 - texte_game_over.get_height()//2 - 100))
            screen.blit(texte_quitter, (screen.get_width()//2 - texte_quitter.get_width()//2,screen.get_height()//2 - texte_quitter.get_height()//2))
    pygame.display.update()

sys.exit()
