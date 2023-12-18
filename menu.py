import pygame

class Menu:
    # Mettre une image (logo du jeu) en haut centrer puis mettre un bouton Jouer en dessous centrer
    def __init__(self):
        self.image = pygame.image.load("Sprite/menu.png")
        self.image_rect = self.image.get_rect()
        self.image_rect.x = 50
        self.image_rect.y = 0

        self.play_button = pygame.image.load("Sprite/playButton.png")
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x = 50
        self.play_button_rect.y = 150

        self.image_game_over = pygame.image.load("Sprite/gameOver.jpg")
        #scale the image to the size of the screen
        self.image_game_over = pygame.transform.scale(self.image_game_over, (300, 300))
        self.image_game_over_rect = self.image_game_over.get_rect()
        self.image_game_over_rect.x = 75
        self.image_game_over_rect.y = -75


    def draw_start_menu(self, screen):
        # afficher l'image en haut centrer puis mettre un bouton jouer en dessous
        screen.blit(self.image, self.image_rect)
        screen.blit(self.play_button, self.play_button_rect)
        pygame.display.flip()


    def draw_game_over(self, screen):
        #background blanc
        screen.fill((255, 255, 255))
        # afficher l'image en haut centrer puis mettre un bouton jouer en dessous
        screen.blit(self.image_game_over, self.image_game_over_rect)
        screen.blit(self.play_button, self.play_button_rect)
        pygame.display.flip()


    # si le bouton est cliquer alors on lance le jeu
    def start_game(self, screen, game):
        if game.game_state == "start_menu":
            # Effacer l'écran pour pouvoir afficher le jeu
            screen.fill((0, 0, 0))
            game.game_state = "playing"

    