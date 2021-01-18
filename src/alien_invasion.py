import sys
import pygame
from settings import Settings
from ship import Ship
import os

class Invaders:

    def __init__(self):
        pygame.init()
        print(os.getcwd())
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Invaders")
        self.ship = Ship(self)
        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(self.bg_color)
            self.ship.draw()
            pygame.display.flip()


if __name__ == '__main__':
    invaders = Invaders()
    invaders.run_game()
