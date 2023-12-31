import pygame


class Score:

  def __init__(self, x):
    self.score = x
    #self.image = pygame.image.load("score.png")

  def score_add(self, x):
    self.score += x

  def display(self, screen, x, y):
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(self.score), 1, (255, 255, 255))
    screen.blit(text, (x, y))

  def get_score(self):
    return self.score

  def reset(self):
    self.score = 0
