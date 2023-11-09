import pygame
from score import Score

class Food:

  def __init__(self, x, y, s):
    self.x = x
    self.y = y
    self.score = s
    self.actif = True
    #self.image = pygame.image.load("food.png")

  def eat(self, type):
    if type == 2:
      self.score.score_add(15)
      self.actif = False
    elif type == 3:
      self.score.score_add(50)
      self.actif = False
      #Effectuer le pouvoir de la grosse pacgomme