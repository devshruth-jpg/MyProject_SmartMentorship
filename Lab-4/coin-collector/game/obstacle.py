
"""
Obstacle: a rectangular object that damages the player on contact.
"""

import pygame


class Obstacle:
    def __init__(
        self,
        x,
        y,
        width=50,
        height=30,
        color=(190, 65, 65),
    ):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def get_rect(self):
        return self.rect
