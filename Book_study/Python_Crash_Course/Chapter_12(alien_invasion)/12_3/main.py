import sys
import pygame

from settings import Settings
from ship import Ship
import game_function as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))   # 创建名为screen的显示窗口
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)

    while True:
        gf.check_events(ship)
        ship.updata()
        gf.update_screen(ai_settings, screen, ship)




run_game()