"""
shoot.py
"""
import pygame

from circleshape import CircleShape
from constants import SHOOT_RADIUS

class Shot(CircleShape):
    """
    Shoot class
    """

    def __init__(self, position:pygame.Vector2):
        super().__init__(position.x, position.y, SHOOT_RADIUS)

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
        Update shot position following a constant speed through a
        straight line
        """
        self.position += self.velocity * dt
