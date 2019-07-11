import sys
import pygame

from settings import Settings
import key as kkey


def display():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))   # 创建名为screen的显示窗口
    pygame.display.set_caption("Display")
    ai_settings.update_screen(screen)

    while True:
        kkey.check_key()

display()