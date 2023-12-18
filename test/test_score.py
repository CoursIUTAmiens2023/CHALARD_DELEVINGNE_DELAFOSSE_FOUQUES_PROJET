import unittest
import pygame

from score import Score

class TestScore(unittest.TestCase):

    def setUp(self):
        # Initialisation pour les tests
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.score = Score(0)

    def test_score_add(self):
        # Test de la méthode score_add
        self.score.score_add(10)
        self.assertEqual(self.score.get_score(), 10)

    def test_display(self):
        # Test de la méthode display
        self.score.score_add(5)
        self.score.display(self.screen, 100, 100)
        pygame.display.flip()  
        pygame.time.delay(2000)  

    def test_reset(self):
        self.score.score_add(15)
        self.score.reset()
        self.assertEqual(self.score.get_score(), 0)

    def tearDown(self):
        # Nettoyage après les tests
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
