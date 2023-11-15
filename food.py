import pygame
from score import Score

class PacGomme(pygame.sprite.Sprite):
    def __init__(self, x, y, image, points, donne_pouvoir):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.points = points
        self.donne_pouvoir = donne_pouvoir