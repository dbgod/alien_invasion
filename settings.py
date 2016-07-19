class Settings():
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's static settings."""
        # Frame rate
        self.fps = 60

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3
        
        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10
        
        # Laser settings
        self.laser_width = 3
        self.laser_height = 20
        self.laser_color = (0, 0, 120)

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5
        
        # Scoring
        self.alien_points = 50
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Initialize settings thta change throughout the game."""
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 15
        self.alien_speed_factor = 2
        self.laser_speed_factor = 10
        self.laser_min_ticks = 60
        self.laser_max_ticks = 180

        # float_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.laser_min_ticks = int(self.laser_min_ticks / self.speedup_scale)
        self.laser_max_ticks = int(self.laser_max_ticks / self.speedup_scale)
        self.alien_points = int(self.alien_points * self.score_scale)
