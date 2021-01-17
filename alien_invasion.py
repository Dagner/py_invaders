import sys
import pygame

class Invaders:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Invaders")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            pygame.display.flip()


if __name__ == '__main__':
    invaders = Invaders()
    invaders.run_game()