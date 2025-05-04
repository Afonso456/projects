import pygame
from game import Game

def main():
    """Main entry point for the Snake Game."""
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()

if __name__ == "__main__":
    main()

