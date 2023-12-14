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
        self.x_init = x
        self.y_init = y
        
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
            
        """from collections import deque
        from enum import Enum
        import json

        class Direction(Enum):
            Haut = (-1, 0)
            Bas = (1, 0)
            Gauche = (0, -1)
            Droite = (0, 1)

        def find_shortest_path(matrix, start_x, start_y, flag_x, flag_y):
            rows, cols = len(matrix), len(matrix[0])
            queue = deque()
            visited = [[False] * cols for _ in range(rows)]

            queue.append(Node(start_x, start_y, None))
            visited[start_x][start_y] = True

            while queue:
                current = queue.popleft()

                if current.x == flag_x and current.y == flag_y:
                    return construct_path(current)

                for dir in Direction.__members__.values():
                    new_x, new_y = current.x + dir.value[0], current.y + dir.value[1]

                    if is_valid_move(new_x, new_y, rows, cols) and matrix[new_x][new_y] == 0 and not visited[new_x][new_y]:
                        queue.append(Node(new_x, new_y, current))
                        visited[new_x][new_y] = True

            return []

        def construct_path(destination):
            path = []

            while destination.parent is not None:
                path.append(get_direction(destination.parent, destination))
                destination = destination.parent

            path.reverse()
            return path

        def get_direction(from_node, to_node):
            if from_node.x < to_node.x:
                return "Bas"
            elif from_node.x > to_node.x:
                return "Haut"
            elif from_node.y < to_node.y:
                return "Droite"
            elif from_node.y > to_node.y:
                return "Gauche"
            return ""

        def is_valid_move(x, y, rows, cols):
            return 0 <= x < rows and 0 <= y < cols

        class Node:
            def __init__(self, x, y, parent):
                self.x = x
                self.y = y
                self.parent = parent

        if __name__ == "__main__":
            with open("map.json", "r") as fichier:
            matrix  = json.load(fichier)
            

            start_x, start_y = 7, 7
            flag_x, flag_y = 287, 257
            print("start")
            path = find_shortest_path(matrix, start_x, start_y, flag_x, flag_y)
            print("finish")
            if path:
                print(f"Chemin trouvé : {path}")
            else:
                print("Aucun chemin trouvé.")
        """

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
            

    def resurect(self):
        self.rect.x = self.x_init
        self.rect.y = self.y_init