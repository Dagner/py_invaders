import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
import os

class Invaders:

    def __init__(self):
        pygame.init()
        print(os.getcwd()) # path de ejecución
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Invaders")
        self.ship = Ship(self)
        self.bg_color = (self.settings.bg_color)
        self._init_bullets()
        

    def _init_bullets(self):
        self.bullets = []
        self.bullet_count = 40
        self.bullet_image = pygame.image.load("invaders_game/imgs/bullet.png")
        for _ in range(self.bullet_count):
            new_bullet = Bullet(self)
            self.bullets.append(new_bullet)
        self.bullet_group = pygame.sprite.Group(self.bullets)

    def _fire_bullet(self):
        for bullet in self.bullets:
            if not bullet.is_active:
                bullet.set_position(self.ship.rect.centerx, self.ship.rect.centery)
                bullet.is_active = True
                return

    def _process_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.move_right = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.move_left = True
                    elif event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if event.key == pygame.K_SPACE:
                        self._fire_bullet()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.move_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.move_left = False

    def _update_game(self):
        self.ship.update()
        self.bullet_group.update()

    def _render(self):
        self.screen.fill(self.bg_color)
        for bullet in self.bullet_group.sprites():
            bullet.draw()
        self.ship.draw()
        pygame.display.flip()

    def run_game(self):
        while True:
            self._process_events()
            self._update_game()
            self._render()
            


if __name__ == '__main__':
    invaders = Invaders()
    invaders.run_game()
