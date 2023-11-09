import pygame
from pacman import Pacman
global score

class Game:

  def __init__(self):
    # Initialisation de la fenêtre et d'autres paramètres du jeu
    pygame.init()
    self.screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pacman")
    self.clock = pygame.time.Clock()

  def run(self):
    # Initialisation du score
    global score = 0
    # Initialisation des sprites
    pacman = Pacman(10, 5)
    pacman.draw(self.screen)
    # Boucle principale du jeu

    while True:
      # Vérification des événements
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()
      # Modification

      # Dessin

      # Vérification des collisions

      # Actualisation de l'affichage

      # Temps d'attente

      self.clock.tick(60)
      pygame.display.flip()

  def handle_events(self):
    # Gérer les événements tels que les touches du clavier
    return 0

  def update(self):
    # Mettre à jour la logique du jeu
    return 0

  def draw(self):
    # Dessiner les éléments du jeu sur l'écran
    return 0
