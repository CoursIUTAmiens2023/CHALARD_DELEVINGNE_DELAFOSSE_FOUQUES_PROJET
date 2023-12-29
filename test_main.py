import unittest
import pygame
from pacman import Pacman
from food import PacGomme
from game import Game

class TestGameMethods(unittest.TestCase):
    def setUp(self):
        # Initialisation de pygame avant chaque test
        pygame.init()

    def test_handle_pacman_collisions(self):
        # Teste la méthode handle_pacman_collisions
        pacman = Pacman(0, 0)
        pac_gomme = PacGomme(0, 0)
        game = Game()
        game.pac_gommes.add(pac_gomme)

        # Appel de la méthode à tester
        game.handle_pacman_collisions([pac_gomme])

        # Vérifications avec des assertions
        self.assertNotIn(pac_gomme, game.pac_gommes)
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
