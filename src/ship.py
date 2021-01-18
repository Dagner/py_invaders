import pygame

class Ship:

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load("invaders_game/imgs/ship.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def draw(self):
        self.screen.blit(self.image, self.rect)
