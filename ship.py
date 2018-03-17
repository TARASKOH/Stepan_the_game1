import pygame
class Ship():
    def __init__(self,game_settings, screen):
        self.screen = screen
        self.game_settings = game_settings

        self.image = pygame.image.load('images\ship.png')
        self.image = pygame.transform.scale(self.image, (250, 120))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 9
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= 9
        if self.moving_top and self.rect.top > self.screen_rect.top:
            self.rect.centery -= 9
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 9



