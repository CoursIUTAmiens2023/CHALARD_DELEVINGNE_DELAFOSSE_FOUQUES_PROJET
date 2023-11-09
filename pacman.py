import pygame
from food import Food
from map import Map
from score import Score


class Pacman:

  def __init__(self, x, y, s):
    self.x = x
    self.y = y
    self.dead = False
    self.win = False
    self.score = s
    #self.image = pygame.image.load("pacman.png")
    # Autres attributs et méthodes pour le mouvement, la direction, etc.

  def move(self, dx, dy, position):
    #vérification des murs
    plateau = position.recup_map()
    if plateau[dx][dy] != 0:
      #Vérification si une pacgomme se trouve sur la prochaine case
      pacgomme = Food(dx, dy, self.score)
      pacgomme.eat(plateau[dx][dy])
      #changé case en vide
      position.pacGommeMange(dx,dy)
      #puis on incrémente la position de pacman
      self.x = dx
      self.y = dy

    return 0

  def draw(self, screen, x, y):
    # Couleurs
    jaune = (255, 255, 0)
    pygame.draw.circle(screen, jaune, (int(x), int(y)), 20)
    #screen.blit(self.image, (self.x, self.y))

  # Return si pacman est mort
  def is_dead(self):
    return self.dead

  # Return si pacman a gagné
  def is_win(self):
    return self.win

  # return position de pacman
  def get_position(self):
    return self.x, self.y