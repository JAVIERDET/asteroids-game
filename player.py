"""
player.py
"""
# pylint: disable=no-member
import pygame

from circleshape import CircleShape
from shot import Shot
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN
)

class Player(CircleShape):
    """
    Player class
    """

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        """
        Creates a triangle
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen:pygame.Surface):
        """
        Draw the specified polygon on the screen
        """
        # Draw the triangle
        pygame.draw.polygon(screen, [255, 255, 255], self.triangle(), 2)

    def rotate(self, dt:float):
        """
        Rotate the player (speed * time_between_frames) rotation units
        """
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        """
        Update player postion when keys are pressed
            a -> rotate counterclockwise
            d -> rotate clockwise
            w -> move straightforward
            s -> move backward
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        # Decrease the shooter timer
        self.timer -= dt


    def move(self, dt):
        """
        Move the player (PLAYER_SPEED * dt) units following the direction set
        by self.rotation unit vector
        """

        # Unit vector (x=0, y=1)
        uv = pygame.Vector2(0,1)

        # Rotation
        rot = uv.rotate(self.rotation)

        # Movement
        mov = rot * PLAYER_SPEED * dt

        # Add the movement to the current position
        self.position += mov

    def shoot(self):
        """
        Creates a shoot (Shoot) object and initializes it's speed
        """
        if self.timer > 0:
            return

        # Create a shoot at player's position
        shoot = Shot(self.position)

        # Set the shoot velocity
        init_vector = pygame.Vector2(0,1)
        rot_vector = init_vector.rotate(self.rotation)
        shoot.velocity = rot_vector * PLAYER_SHOOT_SPEED

        # Set the timer to the cooldown constant
        self.timer = PLAYER_SHOOT_COOLDOWN
