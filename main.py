import pygame
import sys
from ghost import Ghost
from pacman import Pacman
from game import Game
from score import Score
from map import Map

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Rond Jaune qui Bouge")

# Couleurs
jaune = (255, 255, 0)

# Position initiale du rond
x, y = largeur // 2, hauteur // 2

# Vitesse du rond
vitesse = 5

lastKeyPressed = None

# Création de l'objet Pacman
map = Map()
score = Score(0)
pacman = Pacman(0, 0, score)

# Boucle principale
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  # Mouvement du rond avec les touches de direction
  touches = pygame.key.get_pressed()
  x += (touches[pygame.K_RIGHT] - touches[pygame.K_LEFT]) * vitesse
  y += (touches[pygame.K_DOWN] - touches[pygame.K_UP]) * vitesse

  # Déplacement du rond en fonction de la touche pressée
  if touches[pygame.K_LEFT]:
    lastKeyPressed = "left"
  elif touches[pygame.K_RIGHT]:
    lastKeyPressed = "right"
  if touches[pygame.K_UP]:
    lastKeyPressed = "up"
  if touches[pygame.K_DOWN]:
    lastKeyPressed = "down"

  #Utilisation de move de la classe Pacman selon la dernière touche pressée
  
  positionPacmanX, postionPacmanY = pacman.get_position()
  if lastKeyPressed == "left":
    pacman.move(positionPacmanX - 1, postionPacmanY, map)
  elif lastKeyPressed == "right":
    pacman.move(positionPacmanX + 1, postionPacmanY, map)
  elif lastKeyPressed == "up":
    pacman.move(positionPacmanX, postionPacmanY - 1, map)
  elif lastKeyPressed == "down":
    pacman.move(positionPacmanX, postionPacmanY + 1, map)
  

  # Rafraîchissement de l'écran
  fenetre.fill((0, 0, 0))  # Fond noir

  # Dessin de l'objet Pacman
  positionPacmanX, postionPacmanY = pacman.get_position()
  pacman.draw(fenetre, positionPacmanX, postionPacmanY)

  # Dessin de l'objet Score
  score.display(fenetre, 50,50)

  pygame.display.flip()

  # Limite de vitesse de la boucle
  pygame.time.Clock().tick(30)