import pygame


class Map:

  def __init__(self):
    #self.GB = pygame.image.load("bordGauche_Bas.png")
    #self.GH = pygame.image.load("bordGauche_Haut.png")
    #self.DB = pygame.image.load("bordDroite_Bas.png")
    #self.DH = pygame.image.load("bordDroite_Haut.png")
    #self.MH = pygame.image.load("murHauteur.png")
    #self.ML = pygame.image.load("murLongueur.png")

 #0=Case Hors jeu ou barrière, 1=Case vide, 2=Case PacGomme, 3=Case GrosPacGomme 4=Cage des fantômes 5=TP 6=Fruit

    # Définir la taille des cases
    self.taille_case = 1.6

    # Définir la carte sous forme de matrice
    with open("map.json", "r") as fichier:
      self.plateau = json.load(fichier)
  

  def get_map(self):
    return self.plateau

  def get_size(self):
    return self.taille_case

  def carte(self):
    for index in range(len(self.plateau)):
      case = self.plateau[index]

  def recup_map(self):
    return self.plateau

  def pacGommeMange(self, x, y):
    self.plateau[x][y] = 1
