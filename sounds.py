import pygame

class Sounds():
    """Sound library class."""
    def __init__(self):
        """Initialize sound library."""
        # Ship shoot
        self._ship_shoot = pygame.mixer.Sound('sounds/ship_shoot.wav')
        self._ship_shoot.set_volume(0.5)

        # Ship hit
        self._ship_hit = pygame.mixer.Sound('sounds/ship_hit.wav')
        self._ship_hit.set_volume(0.5)

        # Alien shoot
        self._alien_shoot = pygame.mixer.Sound('sounds/alien_shoot.wav')
        self._alien_shoot.set_volume(0.5)

        # Alien hit
        self._alien_hit = pygame.mixer.Sound('sounds/alien_hit.wav')
        self._alien_hit.set_volume(0.5)

    def ship_shoot(self):
        """Play ship shoot sound."""
        self._ship_shoot.play()

    def ship_hit(self):
        """Play ship hit sound."""
        self._ship_hit.play()

    def alien_shoot(self):
        """Play alien shoot sound."""
        self._alien_shoot.play()

    def alien_hit(self):
        """Play alien hit sound."""
        self._alien_hit.play()
