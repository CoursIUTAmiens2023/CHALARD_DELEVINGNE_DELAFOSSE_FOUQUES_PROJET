import pygame
from map import Map
import random
from Direction import ShortestPathFinder
global score

class Fantome(pygame.sprite.Sprite):
    def __init__(self, x, y, image, carte):
        super().__init__()
        self.image = pygame.image.load(image)
        self.imageStart = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 'Gauche'
        self.changing_direction = False  # Nouvelle variable d'état
        self.carte = carte
        self.x_init = x
        self.y_init = y
        
    def poursuite(self, player):
        matrix = Map().get_map()

        start_x, start_y = self.rect.y, self.rect.x
        flag_x, flag_y = player.rect.y, player.rect.x

        path_finder = ShortestPathFinder()
        path = path_finder.find_shortest_path(matrix, start_x, start_y, flag_x, flag_y)
        
        directions = {'Gauche': (-1, 0), 'Droite': (1, 0), 'Haut': (0, -1), 'Bas': (0, 1)}

        if path:
            next_direction = path[0]
            move_x, move_y = directions.get(next_direction, (0, 0))

            self.rect.x += move_x
            self.rect.y += move_y
   
    def poursuiteclyde(self, player):
            matrix=Map().get_map()
        
            start_x, start_y = self.rect.y, self.rect.x
            flag_x, flag_y = player.rect.y, player.rect.x

            path_finder = ShortestPathFinder()
            path = path_finder.find_shortest_path(matrix, start_x, start_y, flag_x, flag_y)
            
            if self.direction == 'Gauche' and matrix[self.rect.y][self.rect.x - 1] == 1:
                if matrix[self.rect.y - 1][self.rect.x] == 1:
                    self.direction = random.choice(['Droite', 'Bas'])
                elif matrix[self.rect.y + 1][self.rect.x] == 1:
                    self.direction = random.choice(['Droite', 'Haut'])
                else :
                    self.direction = random.choice(['Droite', 'Haut', 'Bas'])
                
            elif self.direction == 'Droite' and matrix[self.rect.y][self.rect.x + 1] == 1:
                if matrix[self.rect.y - 1][self.rect.x] == 1:
                    self.direction = random.choice(['Droite', 'Bas'])
                elif matrix[self.rect.y + 1][self.rect.x] == 1:
                    self.direction = random.choice(['Droite', 'Haut'])
                else :
                    self.direction = random.choice(['Droite', 'Haut', 'Bas'])
            elif self.direction == 'Haut' and matrix[self.rect.y - 1][self.rect.x] == 1:
                if matrix[self.rect.y][self.rect.x - 1] == 1:
                    self.direction = random.choice(['Droite', 'Bas'])
                elif matrix[self.rect.y][self.rect.x + 1] == 1:
                    self.direction = random.choice(['Gauche', 'Bas'])
                else:
                    self.direction = random.choice(['Gauche', 'Droite', 'Bas'])

            elif self.direction == 'Bas' and matrix[self.rect.y + 1][self.rect.x] == 1:
                if matrix[self.rect.y][self.rect.x - 1] == 1:
                    self.direction = random.choice(['Droite', 'Haut'])
                elif matrix[self.rect.y][self.rect.x + 1] == 1:
                    self.direction = random.choice(['Gauche', 'Haut'])
                else:
                    self.direction = random.choice(['Gauche', 'Droite', 'Haut'])
            
            if len(path) <= 9:
                path = path_finder.find_shortest_path(matrix, start_x, start_y, flag_x, flag_y)
            if self.direction == 'Gauche' :
                self.rect.x -= 1
            elif self.direction == 'Droite' :
                self.rect.x += 1
            elif self.direction == 'Haut' :
                self.rect.y -= 1
            elif self.direction == 'Bas' :
                self.rect.y += 1

    def update(self, player, fenetre, taille_case, game):
        # Gestion poursuites selon les fantomes
        if self == game.blinky:
            self.poursuite(player)
        if self == game.pinky:
            self.poursuite(player)
        if self == game.inky:
            self.poursuite(player)
        if self == game.clyde:
            self.poursuiteclyde(player)
            
        fenetre.blit(self.image, (self.rect.x * taille_case, self.rect.y * taille_case))
        


    def resurect(self):
        self.rect.x = self.x_init
        self.rect.y = self.y_init


    def scared(self):
        self.image = pygame.image.load("Sprite/Fantometouche.png")

    def normal(self):
        self.image = self.imageStart