#Crée par Louis-Léandre DEMARE le 9/11/2022

import pygame

class Phase:
    """
    Création d'un instance Phase : Phase(screen)
    
    attribut d'instance :
        screen = l'ecran sur lequel est projeté le jeu
    arrtibut de classe :
        méthode :
            game_over(etat), prend en parametre un etat de type str
            win(etat), prend en parametre un etat de type str
    """
    def __init__(self, screen) -> None:
        self.screen = screen
        
    def game_over(self, etat:str):
        if etat == "dead":
            self.screen.fill([0,0,0])
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return False
                    if event.type == pygame.QUIT:
                        return False
            font = pygame.font.Font('font/game_over.ttf', 128)
            texte_game_over = font.render('Oh non tu as perdu... ', True, (255,0,0))
            texte_encouragement = font.render('Tu feras mieux la prochaine fois', True, (255,255,255))
            texte_quitter = font.render('Appuie sur \'echap\' quitter', True, (128,128,128))
            self.screen.blit(texte_game_over, (self.screen.get_width()//2 - texte_game_over.get_width()//2,self.screen.get_height()//2 - texte_game_over.get_height()//2-100))
            self.screen.blit(texte_encouragement, (self.screen.get_width()//2 - texte_encouragement.get_width()//2,self.screen.get_height()//2 - texte_encouragement.get_height()//2))
            self.screen.blit(texte_quitter, (self.screen.get_width()//2 - texte_quitter.get_width()//2,self.screen.get_height()//2 - texte_quitter.get_height()//2+100))
        return True
    def win(self, etat:str):
        if etat == "win":
            self.screen.fill([0,0,0])
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return False
                    if event.type == pygame.QUIT:
                        return False
            font = pygame.font.Font('font/game_over.ttf', 128)
            texte_game_over = font.render('Bravo, tu as gagné contre le boss !', True, (0,255,0))
            texte_quitter = font.render('Appuie sur la touche \'echap\' pour quitter ', True, (128,128,128))
            self.screen.blit(texte_game_over, (self.screen.get_width()//2 - texte_game_over.get_width()//2,self.screen.get_height()//2 - texte_game_over.get_height()//2 - 100))
            self.screen.blit(texte_quitter, (self.screen.get_width()//2 - texte_quitter.get_width()//2,self.screen.get_height()//2 - texte_quitter.get_height()//2))
        return True