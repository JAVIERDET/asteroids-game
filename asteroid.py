"""
asteroid.py
"""
import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    """
    Asteroid class
    """

    def draw(self, screen:pygame.Surface):
        """
        Draw the specified circle on the screen
        """
        pygame.draw.circle(
            screen,
            [255, 255, 255],
            self.position,
            self.radius,
            width=2
        )

    def update(self, dt:float):
        """
        Update asteriod position following a constant speed through a
        straight line
        """
        self.position += self.velocity * dt

    def split(self):
        """
        When a shot is received this method is called and the asteroid:
            - Splits if the radius is greater than ASTEROID_MIN_RADIUS.
            - Dissapears in the other case
        """
        # First kill in any case
        self.kill()

        # If it is a big asteroid
        if self.radius > ASTEROID_MIN_RADIUS:
            rand_angle = random.uniform(20,50)

            # Obtain both asteroids direction angles
            pos_vector = self.velocity.rotate(rand_angle)
            neg_vector = self.velocity.rotate(-rand_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            # Create the two asteroids at the current asteroid position
            ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
            ast_2 = Asteroid(self.position.x, self.position.y, new_radius)

            # Set velocity for both new asteroids
            ast_1.velocity = 1.2 * pos_vector
            ast_2.velocity = 1.2 * neg_vector
