import pygame
from pacman import Pacman


class Game:

  def __init__(self):
    # Initialisation de la fenêtre et d'autres paramètres du jeu
    pygame.init()
    self.screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pacman")
    self.clock = pygame.time.Clock()

  def run(self):
    # Boucle principale du jeu
    running = True
    pacman = Pacman(400, 300)
    while running:
        self.handle_events()
        self.update()
        self.draw()

        # Vérifie si le jeu est fini et met running à False si besoin
        if pacman.is_dead():
          print("Game over")
          running = False
        elif pacman.is_win():
          print("You win!")
          running = False

        #Met à jour l'affichage à 60 fps
        pygame.display.flip()
        self.clock.tick(60)
    
        # Example: if pacman eats all the food, running = False
    return 0

  def handle_events(self):
    # Gérer les événements tels que les touches du clavier
    return 0

  def update(self):
    # Mettre à jour la logique du jeu
    return 0

  def draw(self):
    # Dessiner les éléments du jeu sur l'écran
    return 0
