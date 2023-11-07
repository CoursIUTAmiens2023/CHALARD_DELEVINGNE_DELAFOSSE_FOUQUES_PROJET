import pygame
from score import Score

class Food:
  def __init__(self, x, y, s):
    self.x = x
    self.y = y
    self.actif = True
    self.score = Score(s)
    self.image = pygame.image.load("food.png")

  def eat(self, type):
    if type == "little":
      self.score.score_add(15)
      self.actif = False
    elif type == "big":
      self.score.score_add(50)
      self.actif = False