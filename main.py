import pygame
import sys

from collision import Building
from pacman import Pacman
from food import PacGomme
from game import Game
from map import Map
from menu import Menu

# Initialization
pygame.init()

# Colors
noir = (0, 0, 0)
jaune = (255, 255, 0)
bleu = (0, 0, 255)

# Window size
largeur_map, hauteur_map = 448, 540
fenetre = pygame.display.set_mode((largeur_map, hauteur_map))
pygame.display.set_caption("Pac-Man Game")

# Load background image
bg = pygame.image.load("Sprite/Colision-Map.png").convert()

# Load the map
carte = Map().get_map()

taille_case = Map().get_size()


# Game objects
game = Game()
menu = Menu()
clock = pygame.time.Clock()

# Event handling function
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Functions for different game states
def handle_start_menu():
    global menu  
    menu.draw_start_menu(fenetre)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu.play_button_rect.collidepoint(event.pos):
                menu.start_game(fenetre, game)


def handle_gameplay():
    # Player movement
    handle_player_movement()

    # Update display
    update_display()

# Player movement function
def handle_player_movement():
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT] and carte[game.player.rect.y][game.player.rect.x - 1] != 1:
        game.player.direction = 'left'
    elif touches[pygame.K_RIGHT] and carte[game.player.rect.y][game.player.rect.x + 1] != 1:
        game.player.direction = 'right'
    elif touches[pygame.K_UP] and carte[game.player.rect.y - 1][game.player.rect.x] != 1:
        game.player.direction = 'up'
    elif touches[pygame.K_DOWN] and carte[game.player.rect.y + 1][game.player.rect.x] != 1:
        game.player.direction = 'down'

    update_player_position()

# Update player position function
def update_player_position():
    if game.player.direction == 'left' and carte[game.player.rect.y][game.player.rect.x - 1] != 1:
        game.player.rect.x -= 2
    elif game.player.direction == 'right' and carte[game.player.rect.y][game.player.rect.x + 1] != 1:
        game.player.rect.x += 2
    elif game.player.direction == 'up' and carte[game.player.rect.y - 1][game.player.rect.x] != 1:
        game.player.rect.y -= 2
    elif game.player.direction == 'down' and carte[game.player.rect.y + 1][game.player.rect.x] != 1:
        game.player.rect.y += 2

    game.player.update()
    game.pac_gommes.update()
    game.player.teleportation()

# Update display function
def update_display():

    fenetre.fill(noir)
    fenetre.blit(bg, (0, 0))

    game.score.display(fenetre, 10, 510)
    game.vie.display(fenetre, 300, 510)
    for pac_gomme in game.pac_gommes:
        pac_gomme.affichage(fenetre, taille_case)
    # Timer pour mesurer le temps pris par l'affichage des Pac-Gommes
    update_collisions()
    draw_pacman()
    pygame.display.flip()
    clock.tick(30)


# Update collisions function
def update_collisions():
    pacman_collisions = game.player.collisionPacGomme(game.pac_gommes)
    pacman_collisions_ghost = game.player.collisionGhost(game.fantomes)

    if pacman_collisions:
        handle_pacman_collisions(pacman_collisions)

    if game.super_pouvoir:
        handle_super_pouvoir()

    if pacman_collisions_ghost:
        handle_pacman_ghost_collisions(pacman_collisions_ghost)

    update_ghosts()
    

# Handle pacman collisions function
def handle_pacman_collisions(pacman_collisions):
    for pac_gomme in pacman_collisions:
        game.pac_gommes.remove(pac_gomme)
        game.score.score_add(pac_gomme.points)
        if pac_gomme.donne_pouvoir:
            for fantome in game.fantomes:
                fantome.scared()
            game.super_pouvoir = True
            game.super_pouvoir_timer = pygame.time.get_ticks()

# Handle super pouvoir function
def handle_super_pouvoir():
    now = pygame.time.get_ticks()
    if now - game.super_pouvoir_timer > 5000:
        game.super_pouvoir = False
        for fantome in game.fantomes:
            fantome.normal()

# Handle pacman ghost collisions function
def handle_pacman_ghost_collisions(pacman_collisions_ghost):
    if game.super_pouvoir:
        for ghost in pacman_collisions_ghost:
            ghost.resurect()
            game.score.score_add(200)
    else:
        game.vie.vie_remove(1)
        if game.vie.vie == 0:
            game.game_state = "game_over"
        else:
            game.player.resurect()
            for fantome in game.fantomes:
                fantome.resurect()
                
def update_ghosts():

    for fantome in game.fantomes:
        fantome.update(game.player, fenetre, taille_case, game)
        

# Draw pacman function
def draw_pacman():
    fenetre.blit(game.player.image, (game.player.rect.x * taille_case, game.player.rect.y * taille_case))

# Main game loop
while True:


    handle_events()

    if game.game_state == "start_menu":
        handle_start_menu()
    elif game.game_state == "game_over":
        menu.draw_game_over(fenetre)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu.play_button_rect.collidepoint(event.pos):
                    game = Game()
                    menu = Menu()
                    menu.start_game(fenetre, game)
    else:
        handle_gameplay()

    
# Quit the game
pygame.quit()
sys.exit()
