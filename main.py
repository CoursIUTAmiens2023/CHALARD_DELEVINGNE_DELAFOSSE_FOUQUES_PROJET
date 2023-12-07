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
        game.player.rect.x -= 1
    elif game.player.direction == 'right' and carte[game.player.rect.y][game.player.rect.x + 1] != 1:
        game.player.rect.x += 1
    elif game.player.direction == 'up' and carte[game.player.rect.y - 1][game.player.rect.x] != 1:
        game.player.rect.y -= 1
    elif game.player.direction == 'down' and carte[game.player.rect.y + 1][game.player.rect.x] != 1:
        game.player.rect.y += 1

   
     # Appelle la fonction pour animer Pac-Man avec la direction
    game.player.update()

    # Appelle la fonction pour téléporter Pac-Man en fonction de sa localisation
    game.player.teleportation()
    # Dessiner la carte
    for i in range(len(carte)):
        for j in range(len(carte[i])):
            if carte[i][j] == 1:
                pygame.draw.rect(fenetre, bleu, (j * taille_case, i * taille_case, taille_case, taille_case))
    
    # Rafraîchir l'écran
    fenetre.blit(bg, (0, 0))    
    
     # Fonction de poursuite des fantômes
    for fantome in game.fantomes:
        fantome.update(game.player)
        
    game.fantomes.draw(fenetre)
    # Dessiner Pac-Man
    fenetre.blit(game.player.image, (game.player.rect.x * taille_case, game.player.rect.y * taille_case))
    game.fantomes.draw(fenetre)
    fenetre.blit(game.blinky.image,(game.blinky.rect.x * taille_case, game.blinky.rect.y * taille_case))
    pygame.display.flip()

    # Limiter la vitesse du jeu
    pygame.time.Clock().tick(30)
