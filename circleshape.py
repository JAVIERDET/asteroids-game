"""
circleshape.py
"""

from __future__ import annotations

import pygame

class CircleShape(pygame.sprite.Sprite):
    """
    Base class for game objects
    """
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen:pygame.Surface):
        """
        Drawing class that sub-classes must override
        """

    def update(self, dt):
        """
        Updating class that sub-classes must override
        """

    def collision(self, entity:CircleShape):
        """
        Method for calculating collision events.
        Returns True if the distance between centers is smaller that the added radius.
        """
        distance = self.position.distance_to(entity.position)
        # distance = self.position - entity.position

        if distance > self.radius + entity.radius:
            return False

        return True
