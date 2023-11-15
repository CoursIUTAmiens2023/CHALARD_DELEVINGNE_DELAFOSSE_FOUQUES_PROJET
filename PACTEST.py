import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Définir les couleurs
noir = (0, 0, 0)
blanc = (255, 255, 255)

# Définir la taille de la fenêtre
largeur_map, hauteur_map = 448, 496
fenetre = pygame.display.set_mode((largeur_map, hauteur_map))
pygame.display.set_caption("Pac-Man Game")

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite_sheet):
        super().__init__()
        self.velocity = 2
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

class PacGomme(pygame.sprite.Sprite):
    def __init__(self, x, y, image, points, donne_pouvoir):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.points = points
        self.donne_pouvoir = donne_pouvoir
        
class Fantome(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 'left'
        self.changing_direction = False  # Nouvelle variable d'état

    def poursuite(self, player):
        target_x = player.rect.x
        target_y = player.rect.y

        possible_directions = []

        # Vérifier les directions possibles en fonction de la cible
        if target_x < self.rect.x and not game.check_collision(self, game.wall_left):
            possible_directions.append('left')
        elif target_x > self.rect.x and not game.check_collision(self, game.wall_right):
            possible_directions.append('right')

        if target_y < self.rect.y and not game.check_collision(self, game.wall_up):
            possible_directions.append('up')
        elif target_y > self.rect.y and not game.check_collision(self, game.wall_down):
            possible_directions.append('down')

        # Si le fantôme est actuellement bloqué dans sa direction, il choisit une nouvelle direction
        if self.direction not in possible_directions or self.changing_direction:
            # Choisir une nouvelle direction en fonction de la position du joueur
            if player.rect.y < self.rect.y and not game.check_collision(self, game.wall_up):
                self.direction = 'up'
            elif player.rect.y > self.rect.y and not game.check_collision(self, game.wall_down):
                self.direction = 'down'
            elif player.rect.x < self.rect.x and not game.check_collision(self, game.wall_left):
                self.direction = 'left'
            elif player.rect.x > self.rect.x and not game.check_collision(self, game.wall_right):
                self.direction = 'right'

            self.changing_direction = False

    def update(self, player):
        # Choix de la fonction de poursuite en fonction du fantôme
        self.poursuite(player)

        # Gestion des collisions avec les murs en fonction de la direction
        if not self.changing_direction:
            if self.direction == 'left' and game.check_collision(self, game.wall_left):
                self.try_change_direction('left', ['up', 'down'])
            elif self.direction == 'right' and game.check_collision(self, game.wall_right):
                self.try_change_direction('right', ['up', 'down'])
            elif self.direction == 'up' and game.check_collision(self, game.wall_up):
                self.try_change_direction('up', ['left', 'right'])
            elif self.direction == 'down' and game.check_collision(self, game.wall_down):
                self.try_change_direction('down', ['left', 'right'])

            # Si le fantôme est toujours bloqué, choisir une nouvelle direction
            if game.check_collision(self, game.wall_left) and game.check_collision(self, game.wall_right) and \
                    game.check_collision(self, game.wall_up) and game.check_collision(self, game.wall_down):
                self.changing_direction = True

        # Gestion des collisions avec les murs en fonction de la direction
        if not self.changing_direction:
            if self.direction == 'left' and not game.check_collision(self, game.wall_left):
                self.rect.x -= 1
            elif self.direction == 'right' and not game.check_collision(self, game.wall_right):
                self.rect.x += 1
            elif self.direction == 'up' and not game.check_collision(self, game.wall_up):
                self.rect.y -= 1
            elif self.direction == 'down' and not game.check_collision(self, game.wall_down):
                self.rect.y += 1

        # Réinitialiser l'état de changement de direction après avoir traversé un mur
        self.changing_direction = False

    def try_change_direction(self, new_direction, forbidden_directions):
        # Choisir une nouvelle direction si le fantôme est actuellement bloqué dans une direction interdite
        if self.direction in forbidden_directions:
            self.direction = new_direction


            
class Building(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Game:
    def __init__(self):
        pacman_spritesheet = pygame.image.load("Sprite.png").convert()
        self.player = Player(50, 50, pacman_spritesheet)

        # Création des colisions 
        self.wall_left = pygame.sprite.Group()
        self.wall_up = pygame.sprite.Group()
        self.wall_down = pygame.sprite.Group()
        self.wall_right = pygame.sprite.Group()

        self.wall_left.add(Building('Colision-Map-gauche.png', 0, 0))
        self.wall_up.add(Building('Colision-Map-haut.png', 0, 0))
        self.wall_down.add(Building('Colision-Map-bas.png', 0, 0))
        self.wall_right.add(Building('Colision-Map-droite.png', 0, 0))

        # Création des pac-gommes 
        self.pac_gommes = pygame.sprite.Group()
        self.pac_gommes.add(PacGomme(50, 50, 'Point.png', 10, False))
        self.pac_gommes.add(PacGomme(200, 200, 'Pac-Gomme.png', 50, True))
        self.pac_gommes.add(PacGomme(300, 300, 'Point.png', 10, False))

        # Création des fantômes
        self.fantomes = pygame.sprite.Group()
        self.blinky = Fantome(50, 50, 'Fantome.png')
        self.pinky = Fantome(150, 150, 'Fantome.png')
        self.inky = Fantome(200, 200, 'Fantome.png')
        self.clyde = Fantome(250, 250, 'Fantome.png')
        
        self.fantomes.add(self.blinky,self.pinky, self.inky, self.clyde)
        
        # Définition des fantômes principaux
        self.blinky = self.fantomes.sprites()[0]
        self.pinky = self.fantomes.sprites()[1]
        self.inky = self.fantomes.sprites()[2]
        self.clyde = self.fantomes.sprites()[3]
        
        
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
   
            
            
# Charger l'image de fond
bg = pygame.image.load("Colision-Map.png").convert()

# Position initiale
direction = ''
game = Game()


# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Gestion des déplacements
    touches = pygame.key.get_pressed()

    # Sauvegarde des anciennes coordonnées du joueur
    ancien_x, ancien_y = game.player.rect.x, game.player.rect.y

    if touches[pygame.K_LEFT]:
        game.player.move('left')
        direction = 'left'
    elif touches[pygame.K_RIGHT]:
        game.player.move('right')
        direction = 'right'
    elif touches[pygame.K_UP]:
        game.player.move('up')
        direction = 'up'
    elif touches[pygame.K_DOWN]:
        game.player.move('down')
        direction = 'down'

    # Vérifie la collision avec les murs en fonction de la direction
    if direction == 'left' and game.check_collision(game.player, game.wall_left):
        game.player.rect.x = ancien_x
    elif direction == 'right' and game.check_collision(game.player, game.wall_right):
        game.player.rect.x = ancien_x
    elif direction == 'up' and game.check_collision(game.player, game.wall_up):
        game.player.rect.y = ancien_y
    elif direction == 'down' and game.check_collision(game.player, game.wall_down):
        game.player.rect.y = ancien_y

    # Appelle la fonction pour animer Pac-Man avec la direction
    game.player.update()

    # Appelle la fonction pour téléporter Pac-Man en fonction de sa localisation
    game.player.teleportation()

    # Rafraîchir l'écran
    fenetre.blit(bg, (0, 0))  # Blitter l'image de fond
    fenetre.blit(game.player.image, (game.player.rect.x, game.player.rect.y))
    
     # Fonction de poursuite des fantômes
    for fantome in game.fantomes:
        fantome.update(game.player)
        
    # Afficher les pac-gommes
    game.pac_gommes.draw(fenetre)
    game.fantomes.draw(fenetre)
    pygame.display.flip()

    # Limiter la vitesse du jeu
    pygame.time.Clock().tick(30)
