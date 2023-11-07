import pygame
from food import Food
from map import Map


class Pacman:
  def __init__(self, x, y):
      self.x = x
      self.y = y
      self.image = pygame.image.load("pacman.png")
      # Autres attributs et méthodes pour le mouvement, la direction, etc.
  
  def move(self, dx, dy):
    #vérification des murs
    #faudrait rendre plato public pour y avoir acces dans les move je pense
    if Map.plateau[dx,dy] != 0:
      #Vérification si une pacgomme se trouve sur la prochaine case
      pacgomme = Food(dx, dy)
      pacgomme.eat(Map.plateau[dx,dy])
      #puis on incrémente la position de pacman 
      self.x += dx
      self.y += dy
    
    return 0