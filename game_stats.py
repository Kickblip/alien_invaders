class GameStats:
    """Track statistic for Alien Invaders"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Stat Alien Invaders in an inactive state
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit