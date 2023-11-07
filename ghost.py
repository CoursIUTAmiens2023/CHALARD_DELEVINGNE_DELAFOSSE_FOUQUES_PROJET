import pygame

class Ghost:
  def __init__(self, x, y):
      self.x = x
      self.y = y
      self.image = pygame.image.load("ghost.png")
      # Autres attributs et méthodes pour le mouvement, la direction, etc.
