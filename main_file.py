import pygame, sys
from settings import Settings
from ship import  Ship
import game_function as g_f
from pygame.sprite import Group
from background import Background
from alien import Alien





def init_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_heidth,))
    aliens = Group()
    ship = Ship(game_settings, screen)
    bullets = Group()
    background = Background(screen)
    pygame.display.set_caption('CHEREPAHA')
    g_f.create_fleet(game_settings, screen, aliens, ship)
    while True:

        g_f.update_screen(game_settings, aliens, screen, ship, bullets,background)

        ship.update()
        g_f.check_events(game_settings, screen, ship, bullets)


        g_f.update_bullets(bullets)



init_game()