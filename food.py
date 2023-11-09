import pygame
global score

class Food:

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.actif = True
    self.image = pygame.image.load("food.png")

  def eat(self, type):
    if type == 1:
      score += 15
      #self.score.score_add(15)
      self.actif = False
    elif type == 2:
      score += 50
      #self.score.score_add(50)
      self.actif = False