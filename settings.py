import pygame


class Settings ():
    pygame.init()
    # Класс для хранения всех настроек игры Alien Invasion.
    def __init__(self):
        # Инициализирует настройки игры.
        # Параметры экрана.

        self.screen_width = 1920
        self.screen_height = 1080
        self.ship_speed_factor = 15
        self.bullet_speed_factor = 35
        self.bullet_width = 4
        self.bullet_height = 10
        self.bullet_color = 255, 255, 255
        self.bullet_allowed = 3
