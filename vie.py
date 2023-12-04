import pygame


class Vie:

  def __init__(self, x):
    self.vie = x
    self.oneup = x
    self.image_pacman = pygame.image.load("Sprite/PacMan-seul.png")
    #self.image = pygame.image.load("score.png")

  def vie_add(self, x):
    #Limiter la vie à 5
    if(self.vie != 5):
      self.vie += x

  def vie_remove(self, x):
    self.vie -= x

  def display(self, screen, x, y):
    # Afficher l'image de PacMan pour chaque vie
    for i in range(self.vie):
        screen.blit(self.image_pacman, (x + i * 30, y))

  def get_score(self):
    return self.vie

  def reset(self):
    self.vie = 3
    self.oneup = 1000
