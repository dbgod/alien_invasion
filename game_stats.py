class GameStats():
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # High score show never be reset
        self.high_score = 0

        # Start Alien Invasion in an inactive state.
        self.game_active = False
    
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit - 1
        self.score = 0
        self.level = 1
        self.laser_ticks = 0
