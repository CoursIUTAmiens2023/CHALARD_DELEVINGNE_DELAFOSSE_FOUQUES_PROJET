import unittest
import pygame
import sys
from pacman import Pacman
from food import PacGomme
from game import Game
from map import Map
from main import handle_events


class TestGameMethods(unittest.TestCase):
    def setUp(self):
        # Initialisation de pygame avant chaque test
        pygame.init()

    def test_handle_pacman_collisions(self):
        # Teste la méthode handle_pacman_collisions
        pygame.init()
        pac_gomme = PacGomme(137, 233, 'Sprite/Point.png', 10, False)
        largeur_map, hauteur_map = 448, 540
        fenetre = pygame.display.set_mode((largeur_map, hauteur_map))
        pygame.display.set_caption("Pac-Man Game")

        # Load the map
        carte = Map().get_map()
        taille_case = Map().get_size()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            game = Game()
            fenetre.fill((0, 0, 0))
            game.game_state = "playing"
    

        # Vérifications avec des assertions
        self.assertEqual(game.score.score, pac_gomme.points)

    def test_handle_super_pouvoir(self):
        game = Game()
        game.super_pouvoir = True
        game.super_pouvoir_timer = pygame.time.get_ticks() - 10000

        # Appel de la méthode à tester
        game.handle_super_pouvoir()

        # Vérification avec une assertion
        self.assertFalse(game.super_pouvoir)

    def test_handle_pacman_ghost_collisions(self):
        game = Game()
        game.super_pouvoir = True
        ghosts = [game.create_ghost() for _ in range(3)]

        # Appel de la méthode à tester
        game.handle_pacman_ghost_collisions(ghosts)

        # Vérifications avec des assertions
        for ghost in ghosts:
            self.assertTrue(ghost.resurrect_called)
        self.assertEqual(game.score.score, 600)

    def tearDown(self):
        # Nettoyage après chaque test
        pygame.quit()

if __name__ == '__main__':
    # Exécution de tous les tests
    unittest.main()
