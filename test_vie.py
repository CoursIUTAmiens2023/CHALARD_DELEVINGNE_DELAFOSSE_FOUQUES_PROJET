import unittest
import pygame

from vie import Vie

class TestVie(unittest.TestCase):

    def setUp(self):
        # Initialisation pour les tests
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.vie = Vie(3)

    def test_vie_add(self):
        # Test de la méthode vie_add
        self.vie.vie_add(2)
        self.assertEqual(self.vie.get_score(), 5) 

    def test_vie_remove(self):
        # Test de la méthode vie_remove
        self.vie.vie_remove(1)
        self.assertEqual(self.vie.get_score(), 2)

    def test_display(self):
        # Test de la méthode display
        self.vie.vie_add(1)
        self.vie.display(self.screen, 100, 100)
        pygame.display.flip()
        pygame.time.delay(2000)

    def test_reset(self):
        # Test de la méthode reset
        self.vie.vie_add(2)
        self.vie.reset()
        self.assertEqual(self.vie.get_score(), 3)  # La vie doit être réinitialisée à 3

    def tearDown(self):
        # Nettoyage après les tests
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
