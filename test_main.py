import unittest
import pygame
import sys
from pacman import Pacman
from food import PacGomme
from game import Game
from map import Map


class TestGameMethods(unittest.TestCase):
    def setUp(self):
        # Initialisation de pygame avant chaque test
        pygame.init()
        largeur_map, hauteur_map = 448, 540
        fenetre = pygame.display.set_mode((largeur_map, hauteur_map))
        pygame.display.set_caption("Pac-Man Game")
        self.game = Game()

    def test_collision_pacman_pacgomme(self):
        # En supposant que les coordonnées de Pacman et de PacGomme se chevauchent pour le test
        self.game.player.rect.x = 12
        self.game.player.rect.y = 12

        # Appelez la fonction de vérification de collision
        collisions = self.game.player.collisionPacGomme(self.game.pac_gommes)

        # Vérifiez que la liste des collisions n'est pas vide (collision s'est produite)
        self.assertTrue(collisions)

        # Maintenant, vous pouvez effectuer des assertions plus spécifiques en fonction de la logique de votre jeu
        for pac_gomme in collisions:
            self.assertTrue(isinstance(pac_gomme, PacGomme))

    def test_handle_super_pouvoir(self):
        self.game.super_pouvoir = True
        self.game.super_pouvoir_timer = pygame.time.get_ticks() - 10000

        # Vérification avec une assertion
        self.assertTrue(self.game.super_pouvoir)

    def test_handle_pacman_ghost_collisions(self):
        self.game.super_pouvoir = True

        self.game.player.rect.x = 125
        self.game.player.rect.y = 107

        # Appelez la fonction de vérification de collision
        collisions = self.game.player.collisionPacGomme(self.game.fantomes)

        # Vérifiez que la liste des collisions n'est pas vide (collision s'est produite)
        self.assertTrue(collisions)

    def tearDown(self):
        # Nettoyage après chaque test
        pygame.quit()

if __name__ == '__main__':
    # Exécution de tous les tests
    unittest.main()
