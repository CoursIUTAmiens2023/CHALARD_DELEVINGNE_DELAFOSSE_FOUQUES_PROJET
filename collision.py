import pygame

from pacman import Pacman
from wall import Wall

class Collision:

    def __init__(self):
        pacman_spritesheet = pygame.image.load("Sprite/Sprite.png").convert()
        self.player = Pacman(50, 50, pacman_spritesheet)
        self.walls = pygame.sprite.Group()
        self.walls.add(Wall('Sprite/Colision-Map-gauche.png', 0, 0))

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)