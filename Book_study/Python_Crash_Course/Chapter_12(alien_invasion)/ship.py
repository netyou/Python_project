import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()   # 飞船的矩形
        self.screen_rect = screen.get_rect()    # 屏幕的矩形

        # 将每艘新飞船放置屏幕底部
        self.rect.centerx = self.screen_rect.centerx    # 将屏幕中心坐标放在飞船上
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:  # self.rect.right返回飞船外接矩形的右边缘的x坐标
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #  根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
