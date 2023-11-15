import pygame
global score

class Fantome(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_debut = x
        self.y_debut = y
        self.direction = 'left'
        self.changing_direction = False  # Nouvelle variable d'état

    def poursuite(self, player, Game):
        target_x = player.rect.x
        target_y = player.rect.y

        possible_directions = []

        # Vérifier les directions possibles en fonction de la cible
        if target_x < self.rect.x and not Game.check_collision(self, Game.wall_left):
            possible_directions.append('left')
        elif target_x > self.rect.x and not Game.check_collision(self, Game.wall_right):
            possible_directions.append('right')

        if target_y < self.rect.y and not Game.check_collision(self, Game.wall_up):
            possible_directions.append('up')
        elif target_y > self.rect.y and not Game.check_collision(self, Game.wall_down):
            possible_directions.append('down')

        # Si le fantôme est actuellement bloqué dans sa direction, il choisit une nouvelle direction
        if self.direction not in possible_directions or self.changing_direction:
            # Choisir une nouvelle direction en fonction de la position du joueur
            if player.rect.y < self.rect.y and not Game.check_collision(self, Game.wall_up):
                self.direction = 'up'
            elif player.rect.y > self.rect.y and not Game.check_collision(self, Game.wall_down):
                self.direction = 'down'
            elif player.rect.x < self.rect.x and not Game.check_collision(self, Game.wall_left):
                self.direction = 'left'
            elif player.rect.x > self.rect.x and not Game.check_collision(self, Game.wall_right):
                self.direction = 'right'

            self.changing_direction = False

    def update(self, player, Game):
        # Choix de la fonction de poursuite en fonction du fantôme
        self.poursuite(player, Game)

        # Gestion des collisions avec les murs en fonction de la direction
        if not self.changing_direction:
            if self.direction == 'left' and Game.check_collision(self, Game.wall_left):
                self.try_change_direction('left', ['up', 'down'])
            elif self.direction == 'right' and Game.check_collision(self, Game.wall_right):
                self.try_change_direction('right', ['up', 'down'])
            elif self.direction == 'up' and Game.check_collision(self, Game.wall_up):
                self.try_change_direction('up', ['left', 'right'])
            elif self.direction == 'down' and Game.check_collision(self, Game.wall_down):
                self.try_change_direction('down', ['left', 'right'])

            # Si le fantôme est toujours bloqué, choisir une nouvelle direction
            if Game.check_collision(self, Game.wall_left) and Game.check_collision(self, Game.wall_right) and \
                    Game.check_collision(self, Game.wall_up) and Game.check_collision(self, Game.wall_down):
                self.changing_direction = True

        # Gestion des collisions avec les murs en fonction de la direction
        if not self.changing_direction:
            if self.direction == 'left' and not Game.check_collision(self, Game.wall_left):
                self.rect.x -= 1
            elif self.direction == 'right' and not Game.check_collision(self, Game.wall_right):
                self.rect.x += 1
            elif self.direction == 'up' and not Game.check_collision(self, Game.wall_up):
                self.rect.y -= 1
            elif self.direction == 'down' and not Game.check_collision(self, Game.wall_down):
                self.rect.y += 1

        # Réinitialiser l'état de changement de direction après avoir traversé un mur
        self.changing_direction = False

    def try_change_direction(self, new_direction, forbidden_directions):
        # Choisir une nouvelle direction si le fantôme est actuellement bloqué dans une direction interdite
        if self.direction in forbidden_directions:
            self.direction = new_direction

    def reaparition(self):
        self.rect.x = self.x_debut
        self.rect.y = self.y_debut