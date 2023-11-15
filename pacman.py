import pygame
from food import PacGomme
from map import Map
from score import Score

# Définir les couleurs
noir = (0, 0, 0)
blanc = (255, 255, 255)

class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite_sheet):
        super().__init__()
        self.velocity = 5
        self.sprite_sheet = sprite_sheet
        self.frame_width = 24
        self.frame_height = 24
        self.total_frames = 2
        self.current_frame = 0
        self.animation_speed = 0.2
        self.last_update = pygame.time.get_ticks()
        self.direction = 'right'

        # Appliquer la couleur noire comme couleur transparente
        self.sprite_sheet.set_colorkey(noir)

        self.image = self.animer_pacman()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_debut = x
        self.y_debut = y

    def move(self, direction):
        self.direction = direction
        if direction == 'left':
            self.rect.x -= self.velocity
        elif direction == 'right':
            self.rect.x += self.velocity
        elif direction == 'up':
            self.rect.y -= self.velocity
        elif direction == 'down':
            self.rect.y += self.velocity

    def animer_pacman(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed * 1000:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % self.total_frames

        frame = pygame.Surface((self.frame_width, self.frame_height), pygame.SRCALPHA)
        frame.blit(self.sprite_sheet, (0, 0), (self.current_frame * self.frame_width, 0, self.frame_width, self.frame_height))

        # Effectue la rotation en fonction de la direction
        if self.direction == 'left':
            frame = pygame.transform.rotate(frame, 180)
        elif self.direction == 'up':
            frame = pygame.transform.rotate(frame, 90)
        elif self.direction == 'down':
            frame = pygame.transform.rotate(frame, -90)

        return frame

    def update(self):
        self.image = self.animer_pacman()
        
    def teleportation(self):
        if(self.rect.x >= 450):
            self.rect.x = -10
        elif(self.rect.x <= -25):
            self.rect.x = 435    

    def reaparition(self):
        self.rect.x = self.x_debut
        self.rect.y = self.y_debut

    def collidePacGomme(self, pac_gommes):
        pac_gommes_collided = pygame.sprite.spritecollide(self, pac_gommes, True)
        points = points = sum(pac_gomme.get_points() for pac_gomme in pac_gommes_collided)
        return pac_gommes_collided, points
    
    def collideGhost(self, fantomes):
        fantomes_collided = pygame.sprite.spritecollide(self, fantomes, False)
        return fantomes_collided