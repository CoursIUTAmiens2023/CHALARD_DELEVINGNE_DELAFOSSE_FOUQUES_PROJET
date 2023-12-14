import pygame
import sys
import random
from collision import Building
from pacman import Pacman
from food import PacGomme
from game import Game
from map import Map

# Initialisation de Pygame
pygame.init()

# Définir les couleurs
noir = (0, 0, 0)
jaune = (255, 255, 0)
bleu = (0, 0, 255)

# Définir la taille de la fenêtre
largeur_map, hauteur_map = 448, 496
fenetre = pygame.display.set_mode((largeur_map, hauteur_map))
pygame.display.set_caption("Pac-Man Game")


# Charger l'image de fond
bg = pygame.image.load("Sprite/Colision-Map.png").convert()

# charger la carte
carte = Map().get_map()
taille_case = Map().get_size()

# Position initiale
direction = ''
game = Game()


# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Gestion des déplacements
    touches = pygame.key.get_pressed()

    if touches[pygame.K_LEFT] and carte[game.player.rect.y][game.player.rect.x - 1] != 1:
        game.player.direction = 'left'
    elif touches[pygame.K_RIGHT] and carte[game.player.rect.y][game.player.rect.x + 1] != 1:
        game.player.direction = 'right'
    elif touches[pygame.K_UP] and carte[game.player.rect.y - 1][game.player.rect.x] != 1:
        game.player.direction = 'up'
    elif touches[pygame.K_DOWN] and carte[game.player.rect.y + 1][game.player.rect.x] != 1:
        game.player.direction = 'down'

    # Met à jour la position de Pac-Man en fonction de la direction
    if game.player.direction == 'left' and carte[game.player.rect.y][game.player.rect.x - 1] != 1:
        game.player.rect.x -= 2
    elif game.player.direction == 'right' and carte[game.player.rect.y][game.player.rect.x + 1] != 1:
        game.player.rect.x += 2
    elif game.player.direction == 'up' and carte[game.player.rect.y - 1][game.player.rect.x] != 1:
        game.player.rect.y -= 2
    elif game.player.direction == 'down' and carte[game.player.rect.y + 1][game.player.rect.x] != 1:
        game.player.rect.y += 2

   
     # Appelle la fonction pour animer Pac-Man avec la direction
    game.player.update()
    game.pac_gommes.update()

    # Appelle la fonction pour téléporter Pac-Man en fonction de sa localisation
    game.player.teleportation()
    # Dessiner la carte
    for i in range(len(carte)):
        for j in range(len(carte[i])):
            if carte[i][j] == 1:
                pygame.draw.rect(fenetre, bleu, (j , i , 1, 1))


    game.score.display(fenetre, 10, 10)
    game.vie.display(fenetre, 300, 10)   
    game.pac_gommes.draw(fenetre)
    
    pacman_collisions = game.player.collisionPacGomme(game.pac_gommes)
    pacman_collisions_ghost = game.player.collisionGhost(game.fantomes)

    # Si une collision est détectée, supprimer la Pac-Gomme et augmenter le score
    if pacman_collisions:
        for pac_gomme in pacman_collisions:
            game.pac_gommes.remove(pac_gomme)
            game.score.score_add(pac_gomme.points)
            if pac_gomme.donne_pouvoir:
                game.super_pouvoir = True
                game.super_pouvoir_timer = pygame.time.get_ticks()

    # si ça fait 5sec que le pouvoir est activé, le désactiver
    if game.super_pouvoir:
        now = pygame.time.get_ticks()
        if now - game.super_pouvoir_timer > 5000:
            game.super_pouvoir = False

    if pacman_collisions_ghost:
        if game.super_pouvoir:
            for ghost in pacman_collisions_ghost:
                ghost.resurect()
                game.score.score_add(200)
        else:
            game.vie.vie_remove(1)
            game.player.resurect()
            for fantome in game.fantomes:
                fantome.resurect()
            

     # Fonction de poursuite des fantômes
    for fantome in game.fantomes:
        fantome.update(game.player)

    print(game.player.rect.x , game.player.rect.y)
    # Dessiner Pac-Man
    fenetre.blit(game.player.image,(game.player.rect.x , game.player.rect.y ))

    #dessiner fantome de game.fantomeEssai
    for fantome in game.fantomes:
        fenetre.blit(fantome.image,(fantome.rect.x, fantome.rect.y))
    
    pygame.display.flip()

    

    # Limiter la vitesse du jeu
    pygame.time.Clock().tick(60)