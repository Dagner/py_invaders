
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = game.bullet_image
        self.rect = self.image.get_rect()
        self.rect.center = (250, 250)
        self.color = (125, 125, 125)
        self.is_active = False
        self.y = float(self.rect.y)
        self.speed = 0.2
        super().__init__()

    def update(self):
        if self.is_active:
            self.y -= self.speed
        if self.rect.midbottom[1] < 0:
            self.is_active = False
        self.rect.centery = self.y

    def draw(self):
        if self.is_active:
            self.screen.blit(self.image, self.rect)

    def set_position(self, x, y):
        self.y = y
        self.rect.center = (x, y)