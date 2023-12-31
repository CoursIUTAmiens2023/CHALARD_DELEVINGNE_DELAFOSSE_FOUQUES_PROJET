import unittest
import pygame
from menu import Menu

class TestMenu(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.menu = Menu()
        self.screen = pygame.display.set_mode((800, 600))

    def test_initialization(self):
        self.assertIsInstance(self.menu, Menu)
        # Ajoutez d'autres assertions pour vérifier l'initialisation d'autres attributs

    def test_draw_start_menu(self):
        # Créer une surface pygame pour tester le rendu
        test_screen = pygame.Surface((800, 600))
        self.menu.draw_start_menu(test_screen)

        # Ajouter des assertions pour vérifier que les éléments sont correctement rendus sur l'écran

    def test_draw_game_over(self):
        # Créer une surface pygame pour tester le rendu
        test_screen = pygame.Surface((800, 600))
        self.menu.draw_game_over(test_screen,0)

        # Ajouter des assertions pour vérifier que les éléments sont correctement rendus sur l'écran

    def test_start_game(self):
        # Créer une instance factice de la classe Game pour le test
        class FakeGame:
            def __init__(self):
                self.game_state = "start_menu"

        fake_game = FakeGame()

        # Créer une surface pygame pour tester le rendu
        test_screen = pygame.Surface((800, 600))

        # Appeler la méthode start_game avec le faux jeu
        self.menu.start_game(test_screen, fake_game)

        # Ajouter des assertions pour vérifier que le jeu change d'état correctement

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
