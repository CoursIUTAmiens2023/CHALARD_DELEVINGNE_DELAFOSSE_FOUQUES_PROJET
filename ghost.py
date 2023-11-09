import pygame
from pacman import Pacman
global score

class Ghost:
  #Initialisation d'un ghost (Clyde / Blinky / Pinky / Inky)
  def __init__(self, x, y, speed, dead=False):
    self.x = x
    self.y = y
    self.speed = speed
    self.dead = dead
    self.image = pygame.image.load("ghost.png")
    # Autres attributs et méthodes pour le mouvement, la direction, etc.

  #Mouvement du ghost
  def move(self, dx, dy):
    self.x += dx * self.speed
    self.y += dy * self.speed

  #Affichage du ghost
  def draw(self, screen):
    screen.blit(self.image, (self.x, self.y))

  #Mort du ghost
  def die(self):
    self.dead = True
    self.image = pygame.image.load("ghost_dead.png")

  #Résurrection du ghost
  def revive(self):
    self.dead = False
    self.image = pygame.image.load("ghost.png")

  #Déplacement du ghost vers pacman en faisant attention aux murs
  def move_to_pacman(self, pacman, walls):
    #regarde selon l'axe x ou y où le fantôme est positionné par rapport à pacman
    if self.x < pacman.x:
      if not self.is_wall(self.x + self.speed, self.y, walls):
        self.move(self.speed, 0)
    elif self.x > pacman.x:
      if not self.is_wall(self.x - self.speed, self.y, walls):
        self.move(-self.speed, 0)
    elif self.y < pacman.y:
      if not self.is_wall(self.x, self.y + self.speed, walls):
        self.move(0, self.speed)
    elif self.y > pacman.y:
      if not self.is_wall(self.x, self.y - self.speed, walls):
        self.move(0, -self.speed)
    return 0

  #Vérifie si le ghost est sur un mur
  def is_wall(self, x, y, walls):
    for wall in walls:
      if wall.x == x and wall.y == y:
        return True
    return False

  #Vérifie si le ghost est sur pacman
  def is_on_pacman(self, pacman):
    return pacman.x == self.x and pacman.y == self.y

  #Vérifie si le ghost est mort
  def is_dead(self):
    return self.dead