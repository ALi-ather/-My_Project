import pygame

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (229, 230, 226)

        # Load the background image
        self.bg_image = pygame.image.load('images/aa.jpg')  # Path to your background image

        # Ship settings
        self.ship_speed = 2.0
        # Bullet settings
        self.bullet_speed = 5.0
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = (173, 216, 230)
        self.bullets_allowed = 4
        # Alien settings
        self.alien_speed = 2.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.ship_limit = 3
