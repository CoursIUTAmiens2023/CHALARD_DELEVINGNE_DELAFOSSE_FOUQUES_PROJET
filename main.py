import pygame
import sys
import random
from collision import Building
from pacman import Pacman
from food import PacGomme
from game import Game

# Initialisation de Pygame
pygame.init()

# Définir les couleurs
noir = (0, 0, 0)
blanc = (255, 255, 255)

# Définir la taille de la fenêtre
largeur_map, hauteur_map = 448, 496
fenetre = pygame.display.set_mode((largeur_map, hauteur_map))
pygame.display.set_caption("Pac-Man Game")


# Charger l'image de fond
bg = pygame.image.load("Sprite/Colision-Map.png").convert()

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

    # Sauvegarde des anciennes coordonnées du joueur
    ancien_x, ancien_y = game.player.rect.x, game.player.rect.y

    if touches[pygame.K_LEFT]:
        game.player.move('left')
        direction = 'left'
    elif touches[pygame.K_RIGHT]:
        game.player.move('right')
        direction = 'right'
    elif touches[pygame.K_UP]:
        game.player.move('up')
        direction = 'up'
    elif touches[pygame.K_DOWN]:
        game.player.move('down')
        direction = 'down'

    # Vérifie la collision avec les murs en fonction de la direction
    if direction == 'left' and game.check_collision(game.player, game.wall_left):
        game.player.rect.x = ancien_x
    elif direction == 'right' and game.check_collision(game.player, game.wall_right):
        game.player.rect.x = ancien_x
    elif direction == 'up' and game.check_collision(game.player, game.wall_up):
        game.player.rect.y = ancien_y
    elif direction == 'down' and game.check_collision(game.player, game.wall_down):
        game.player.rect.y = ancien_y

    # Appelle la fonction pour animer Pac-Man avec la direction
    game.player.update()

    # Appelle la fonction pour téléporter Pac-Man en fonction de sa localisation
    game.player.teleportation()

    # Appelle la fonction vérifiant la collision avec les pac-gommes et retourne un booléen et le nombre de points
    (getPacGomme, points) = game.player.collidePacGomme(game.pac_gommes)
    if(getPacGomme):
        # Update le score en ajoutant 50 points
        game.score.score_add(points)
        # Réaffiche le score
        game.score.display(fenetre, 10, 10)


    # Appelle la fonction vérifiant la collision avec les fantômes et retourne un booléen
    getFantome = game.player.collideGhost(game.fantomes)
    # Si collision avec un fantôme
    if(getFantome):
        # Si le joueur a un super pouvoir
        if(game.super_pouvoir):
            # Supprime le fantôme
            game.fantomes.remove(getFantome)
            # Update le score en ajoutant 200 points
            game.score.score_add(200)
            # Réaffiche le score
            game.score.display(fenetre, 10, 10)
        else:
            # Update le score en ajoutant 50 points
            game.score.score_add(50)
            # Réaffiche le score
            game.score.display(fenetre, 10, 10)
            # Réinitialise la position du joueur
            game.player.reaparition()
            # Réinitialise la position des fantômes
            for fantome in game.fantomes:
                fantome.reaparition()

    # Rafraîchir l'écran
    fenetre.blit(bg, (0, 0))  # Blitter l'image de fond
    fenetre.blit(game.player.image, (game.player.rect.x, game.player.rect.y))
    
     # Fonction de poursuite des fantômes
    for fantome in game.fantomes:
        fantome.update(game.player, game)
        
    # Afficher les pac-gommes
    game.pac_gommes.draw(fenetre)
    # Afficher les fantômes
    game.fantomes.draw(fenetre)
    game.score.display(fenetre, 10, 10)
    pygame.display.flip()

    # Limiter la vitesse du jeu
    pygame.time.Clock().tick(30)
