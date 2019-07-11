class Settings:
    def __init__(self):
        self.screen_width = 1600
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

    def update_screen(self, screen):
        """更新屏幕上的图像，并切换到新屏幕"""
        screen.fill(self.bg_color)