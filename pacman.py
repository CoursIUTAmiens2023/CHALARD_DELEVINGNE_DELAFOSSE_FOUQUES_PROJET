import pygame


class Pacman:
  def __init__(self, x, y):
      self.x = x
      self.y = y
      self.image = pygame.image.load("pacman.png")
      # Autres attributs et méthodes pour le mouvement, la direction, etc.
  
  def move(self, dx, dy):
      self.x += dx
      self.y += dy
      return 0