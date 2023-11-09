import pygame
from food import Food
from map import Map


class Pacman:

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.dead = False
    self.win = False
    self.image = pygame.image.load("pacman.png")
    # Autres attributs et méthodes pour le mouvement, la direction, etc.

  def move(self, dx, dy):
    #vérification des murs
    position = Map(dx,dy)
    plateau = position.recup_map()
    if plateau[dx, dy] != 0:
      #Vérification si une pacgomme se trouve sur la prochaine case
      pacgomme = Food(dx, dy)
      pacgomme.eat(plateau[dx, dy])
      #puis on incrémente la position de pacman
      self.x = dx
      self.y = dy

    return 0

  def draw(self, screen):
    screen.blit(self.image, (self.x, self.y))

  # Return si pacman est mort
  def is_dead(self):
    return self.dead

  # Return si pacman a gagné
  def is_win(self):
    return self.win
