import pygame
from pacman import Pacman
from food import PacGomme
from collision import Building
from ghost import Fantome

class Game:
    def __init__(self):
        pacman_spritesheet = pygame.image.load("Sprite/Sprite.png").convert()
        self.player = Pacman(50, 50, pacman_spritesheet)

        # Création des colisions 
        self.wall_left = pygame.sprite.Group()
        self.wall_up = pygame.sprite.Group()
        self.wall_down = pygame.sprite.Group()
        self.wall_right = pygame.sprite.Group()

        self.wall_left.add(Building('Sprite/Colision-Map-gauche.png', 0, 0))
        self.wall_up.add(Building('Sprite/Colision-Map-haut.png', 0, 0))
        self.wall_down.add(Building('Sprite/Colision-Map-bas.png', 0, 0))
        self.wall_right.add(Building('Sprite/Colision-Map-droite.png', 0, 0))

        # Création des pac-gommes 
        self.pac_gommes = pygame.sprite.Group()
        self.pac_gommes.add(PacGomme(50, 50, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(200, 200, 'Sprite/Pac-Gomme.png', 50, True))
        self.pac_gommes.add(PacGomme(300, 300, 'Sprite/Point.png', 10, False))

        # Création des fantômes
        self.fantomes = pygame.sprite.Group()
        self.blinky = Fantome(50, 50, 'Sprite/Fantome.png')
        self.pinky = Fantome(150, 150, 'Sprite/Fantome.png')
        self.inky = Fantome(200, 200, 'Sprite/Fantome.png')
        self.clyde = Fantome(250, 250, 'Sprite/Fantome.png')
        
        self.fantomes.add(self.blinky,self.pinky, self.inky, self.clyde)
        
        # Définition des fantômes principaux
        self.blinky = self.fantomes.sprites()[0]
        self.pinky = self.fantomes.sprites()[1]
        self.inky = self.fantomes.sprites()[2]
        self.clyde = self.fantomes.sprites()[3]
        
        
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)