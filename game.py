import pygame
from pacman import Pacman
from food import PacGomme
from collision import Building
from ghost import Fantome
from score import Score
from vie import Vie
from map import Map

class Game:
    def __init__(self):
        pacman_spritesheet = pygame.image.load("Sprite/Sprite.png").convert()
        self.player = Pacman(7,7, pacman_spritesheet)

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
        self.pac_gommes.add(PacGomme(12, 12, 'Sprite/Pac-Gomme.png', 50, True))
        self.pac_gommes.add(PacGomme(257, 12, 'Sprite/Pac-Gomme.png', 50, True))
        self.pac_gommes.add(PacGomme(12, 288, 'Sprite/Pac-Gomme.png', 50, True))
        self.pac_gommes.add(PacGomme(257, 288, 'Sprite/Pac-Gomme.png', 50, True))
        self.pac_gommes.add(PacGomme(34, 15, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(50, 15, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(63, 15, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(78, 15, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(93, 15, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(108, 15, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(123, 15, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(123, 34, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(63, 34, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(123, 53, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(15, 53, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(15, 34, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(34, 53, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(50, 53, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(63, 53, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(78, 53, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(93, 53, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(108, 53, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(137, 53, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(152, 53, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(168, 53, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(183, 53, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(199, 53, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(213, 53, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(227, 53, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(243, 53, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(261, 53, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(152, 34, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(213, 34, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(261, 34, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(152, 15, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(168, 15, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(183, 15, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(199, 15, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(213, 15, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(227, 15, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(243, 15, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(261, 15, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(152, 34, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(15, 84, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(34, 84, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(50, 84, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(63, 84, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(93, 84, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(108, 84, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(123, 84, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(152, 84, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(167, 84, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(182, 84, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(213, 84, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(227, 84, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(243, 84, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(261, 84, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(15, 68, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(63, 68, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(93, 68, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(183, 68, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(213, 68, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(261, 68, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(213, 99, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(213, 114, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(213, 129, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(213, 144, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(213, 159, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(213, 174, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(213, 189, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(63, 99, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(63, 114, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(63, 129, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(63, 144, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(63, 159, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(63, 174, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(63, 189, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(15, 203, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(34, 203, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(50, 203, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(63, 203, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(78, 203, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(93, 203, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(108, 203, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(123, 203, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(152, 203, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(168, 203, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(184, 203, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(199, 203, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(213, 203, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(227, 203, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(243, 203, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(261, 203, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(123, 218, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(63, 218, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(15, 218, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(152, 218, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(213, 218, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(261, 218, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(213, 233, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(15, 233, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(34, 233, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(63, 233, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(78, 233, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(93, 233, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(108, 233, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(123, 233, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(152, 233, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(168, 233, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(184, 233, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(199, 233, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(213, 233, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(242, 233, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(261, 233, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(34, 248, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(63, 248, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(93, 248, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(184, 248, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(213, 248, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(242, 248, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(15, 263, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(34, 263, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(50, 263, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(63, 263, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(93, 263, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(108, 263, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(123, 263, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(152, 263, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(168, 263, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(184, 263, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(213, 263, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(228, 263, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(242, 263, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(261, 263, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(15, 278, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(123, 278, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(152, 278, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(261, 278, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(34, 292, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(49, 292, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(63, 292, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(78, 292, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(93, 292, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(108, 292, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(123, 292, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(137, 292, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(152, 292, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(168, 292, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(184, 292, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(199, 292, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(213, 292, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(227, 292, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(243, 292, 'Sprite/Point.png', 10, False))
        self.pac_gommes.add(PacGomme(261, 292, 'Sprite/Point.png', 10, False))
        

        
        # Création des fantômes
        self.fantomes = pygame.sprite.Group()
        self.blinky = Fantome(50, 45, 'Sprite/Fantome.png', Map().get_map())    
        self.pinky = Fantome(10, 10, 'Sprite/Fantome.png', Map().get_map())
        self.inky = Fantome(20, 20, 'Sprite/Fantome.png', Map().get_map())
        self.clyde = Fantome(25, 25, 'Sprite/Fantome.png', Map().get_map())

        self.fantomes.add(self.blinky,self.pinky, self.inky, self.clyde)
        # Création du score
        self.score = Score(0)
        self.vie = Vie(3)
        # Définition des fantômes principaux
        self.blinky = self.fantomes.sprites()[0]
        self.pinky = self.fantomes.sprites()[1]
        self.inky = self.fantomes.sprites()[2]
        self.clyde = self.fantomes.sprites()[3]

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
