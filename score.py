import pygame


class Score:

  def __init__(self, x):
    self.score = x
    self.image = pygame.image.load("score.png")

  def score_add(self, x):
    self.score += x
