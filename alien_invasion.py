import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from sounds import Sounds
import game_functions as gf

def run_game():
    # Initialize game and create a screen object.
	# setup mixer to avoid sound lag
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invastion")
    
    # Instantiate sound library
    sounds = Sounds()
    
    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")
    
    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Make a ship, a group of bullets, a group of aliens, and a group of
    # lasers.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    lasers = Group()
    
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # Create a clock to manage the frame rate
    clock = pygame.time.Clock()
    
    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
			aliens, bullets, sounds)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                bullets)
            gf.check_lasers(ai_settings, screen, stats, aliens, lasers)
            gf.update_lasers(ai_settings, screen, stats, sb, ship, aliens,
                bullets, lasers)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens,
                bullets, lasers)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
            lasers, play_button)

        clock.tick(ai_settings.fps)

run_game()
