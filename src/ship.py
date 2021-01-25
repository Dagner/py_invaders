import pygame
from bullet import Bullet

class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load("invaders_game/imgs/ship.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.speed = 0.3
        self.x = float(self.rect.x)
        self.move_right = False
        self.move_left = False


    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed
        if self.move_left and self.rect.left > 0:
            self.x -= self.speed 
        self.rect.x = self.x
    
    def draw(self):
        self.screen.blit(self.image, self.rect)


