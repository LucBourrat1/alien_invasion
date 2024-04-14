class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # ship settings
        self.ship_speed = 15
        # bullet settings
        self.bullet_speed = 10.0
        self.bullet_width = 8
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10
        # alien settings
        self.alien_speed = 100
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right, -1 represents left
        self.fleet_direction = 1
        self.ship_limit = 3
