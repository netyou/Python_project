import sys
import pygame

from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_height))   # 创建名为screen的显示窗口
    pygame.display.set_caption("Alien Invasion")
    # 创建飞船
    ship = Ship(ai_setting, screen)
    bullets = Group()
    # 设置背景色
    # bg_color = (230, 230, 230)

    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_setting, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        # 每次循环都重绘屏幕
        gf.update_screen(ai_setting, screen, ship,bullets)


run_game()