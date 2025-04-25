# main.py
import pygame
from constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH
)

def main():
    # Initialize pygame
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        # Make the window close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Set backgroung to black
        screen.fill(color="black")
        # Update the full display surface to the screen
        pygame.display.flip()
        
    
if __name__=="__main__":
    main()