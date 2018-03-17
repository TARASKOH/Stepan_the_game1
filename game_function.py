import pygame, sys
from bullet import Bullet
from alien import Alien
from random import randint


def check_events(game_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(game_settings, screen, ship, event, bullets)


def check_keydown_events(game_settings, screen, ship, event, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_top = True
    elif event.key == pygame.K_DOWN:
        ship.moving_bottom = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_UP:
        ship.moving_top = False
    elif event.key == pygame.K_DOWN:
        ship.moving_bottom = False


def update_screen(game_settings, aliens, screen, ship, bullets, background):
    pygame.display.flip()
    background.update()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(game_settings, screen, ship, bullets):
    if len(bullets) < game_settings.bullet_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(game_settings, screen, aliens, ship):
    alien = Alien(game_settings, screen)
    number_aliens_x = get_number_aliens_x(game_settings, alien.rect.width)
    number_aliens_y = get_number_rows(game_settings, alien.rect.height, ship.rect.height)
    random_number = randint(3, 10)


    for rows_number in range(number_aliens_y):
        for alien_number in range(random_number):
            create_alien(game_settings, screen, alien_number, aliens, rows_number)







def get_number_aliens_x(game_settings, alien_width):
    available_space_x = game_settings.screen_width - 1 * alien_width
    number_aliens_x = int(available_space_x / (1 * alien_width))
    return (number_aliens_x)


def get_number_rows(game_settings, alien_height, ship_height):
    available_space_y = game_settings.screen_width - 3 * alien_height - ship_height
    number_aliens_y = int(available_space_y / (2 * alien_height))
    return (number_aliens_y)


def create_alien(game_settings, screen, alien_number, aliens, number_aliens_y):
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.rect.centerx = alien_width + 2 * alien_width * alien_number
    alien.rect.centery = alien.rect.height + 2 * alien.rect.height * number_aliens_y
    aliens.add(alien)
