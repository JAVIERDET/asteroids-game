"""
main.py
"""
# pylint: disable=no-member
import sys

import pygame
from constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH
)
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    """
    Main fucntion
    """
    # Initialize pygame
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Create the screen (Surface object)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create clock and Delta Time variables
    clock = pygame.time.Clock()
    dt = 0

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set the corresponding groups to all instances of the class Player
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Create the player instance
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    # Create an AsteroidField instance
    asteroid_field = AsteroidField()

    while True:
        # Make the window close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Set backgroung to black
        screen.fill(color="black")

        # Update players position before rendering
        for plyr in updatable:
            plyr.update(dt)

        # Re-render players on the screen each frame
        for plyr in drawable:
            plyr.draw(screen)

        # Update the full display surface to the screen
        pygame.display.flip()

        # Check for shot destroying an asteroid
        for ast in asteroids:
            for shot in shots:
                if ast.collision(shot):
                    ast.split()
                    shot.kill()

        # Check for player and asteroid collision
        for ast in asteroids:
            if ast.collision(player):
                sys.exit("Game over!")

        # Pause the game loop for 1/60th of a second and store the dt
        dt = clock.tick(60)/1000

if __name__=="__main__":
    main()
