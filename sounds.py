import pygame

class Sounds():
    """Sound library class."""
    def __init__(self):
        """Initialize sound library."""
        self._ship_shoot = pygame.mixer.Sound('sounds/ship_shoot.wav')

    def ship_shoot(self):
        """Play ship_shoot sound."""
        self._ship_shoot.play()
