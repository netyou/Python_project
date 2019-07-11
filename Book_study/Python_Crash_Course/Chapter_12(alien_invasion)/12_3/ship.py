import pygame
import sys


class Ship:
    """飞机的属性"""

    def __init__(self, ai_settings, screen):
        """飞机属性初始化"""

        self.ai_settings = ai_settings
        self.screen = screen
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.bot = float(self.rect.bottom)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def updata(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.speed_factor
        if self.moving_up and self.rect.top > 0:
            self.bot -= self.ai_settings.speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bot += self.ai_settings.speed_factor

        self.rect.centerx = self.center
        self.rect.bottom = self.bot

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
