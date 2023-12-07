import pygame
from map import Map
global score

class Fantome(pygame.sprite.Sprite):
    def __init__(self, x, y, image, carte):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 'left'
        self.changing_direction = False  # Nouvelle variable d'état
        self.carte = carte
        
    def poursuite(self, player):
        target_x = player.rect.x
        target_y = player.rect.y

        possible_directions = []

        # Vérifier les directions possibles en fonction de la cible
        if target_x < self.rect.x and self.carte[self.rect.y][self.rect.x - 1] != 1:
            possible_directions.append('left')
        elif target_x > self.rect.x and not self.carte[self.rect.y][self.rect.x + 1] != 1:
            possible_directions.append('right')

        if target_y < self.rect.y and self.carte[self.rect.y - 1][self.rect.x] != 1:
            possible_directions.append('up')
        elif target_y > self.rect.y and self.carte[self.rect.y + 1][self.rect.x] != 1:
            possible_directions.append('down')

        # Si le fantôme est actuellement bloqué dans sa direction, il choisit une nouvelle direction
        if self.direction not in possible_directions or self.changing_direction:
            # Choisir une nouvelle direction en fonction de la position du joueur
            if player.rect.y < self.rect.y and self.carte[self.rect.y - 1][self.rect.x] != 1:
                self.direction = 'up'
            elif player.rect.y > self.rect.y and self.carte[self.rect.y + 1][self.rect.x] != 1:
                self.direction = 'down'
            elif player.rect.x < self.rect.x and self.carte[self.rect.y][self.rect.x - 1] != 1:
                self.direction = 'left'
            elif player.rect.x > self.rect.x and self.carte[self.rect.y][self.rect.x + 1] != 1:
                self.direction = 'right'

            self.changing_direction = False

    def update(self, player):
        # Choix de la fonction de poursuite en fonction du fantôme
        self.poursuite(player)

        # Gestion des collisions avec les murs en fonction de la direction
        if not self.changing_direction:
            if self.direction == 'left' and self.carte[self.rect.y][self.rect.x - 1] != 1:
                self.try_change_direction('left', ['up', 'down'])
            elif self.direction == 'right' and self.carte[self.rect.y][self.rect.x + 1] != 1:
                self.try_change_direction('right', ['up', 'down'])
            elif self.direction == 'up' and self.carte[self.rect.y - 1][self.rect.x] != 1:
                self.try_change_direction('up', ['left', 'right'])
            elif self.direction == 'down' and self.carte[self.rect.y + 1][self.rect.x] != 1:
                self.try_change_direction('down', ['left', 'right'])

            # Si le fantôme est toujours bloqué, choisir une nouvelle direction
            if self.carte[self.rect.y][self.rect.x - 1] == 1 and self.carte[self.rect.y][self.rect.x + 1] == 1 and \
                    self.carte[self.rect.y - 1][self.rect.x] == 1 and self.carte[self.rect.y + 1][self.rect.x] == 1:
                self.changing_direction = True

        # Gestion des collisions avec les murs en fonction de la direction
        if not self.changing_direction:
            if self.direction == 'left' and self.carte[self.rect.y][self.rect.x - 1] != 1:
                self.rect.x -= 1
            elif self.direction == 'right' and self.carte[self.rect.y][self.rect.x + 1] != 1:
                self.rect.x += 1
            elif self.direction == 'up' and self.carte[self.rect.y - 1][self.rect.x] != 1:
                self.rect.y -= 1
            elif self.direction == 'down' and self.carte[self.rect.y + 1][self.rect.x] != 1:
                self.rect.y += 1

        # Réinitialiser l'état de changement de direction après avoir traversé un mur
        self.changing_direction = False

    def try_change_direction(self, new_direction, forbidden_directions):
        # Choisir une nouvelle direction si le fantôme est actuellement bloqué dans une direction interdite
        if self.direction in forbidden_directions:
            self.direction = new_direction