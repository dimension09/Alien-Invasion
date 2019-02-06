import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_function as gf

def run_game ():
    # Инициализирует pygame, settings и объект экрана.
    pygame.init() # init() инициализирует настройки, необходимые Pygame для нормальной работы.           
    ai_settings = Settings()
    # Объект screen называется поверхностью (surface).
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # pygame.display.set_mode() создает отображаемую область screen, на которой прорисовываются все графические элементы игры
    pygame.display.set_caption("Alien Invasion")

    # Создание корабля.
    ship = Ship(ai_settings, screen)
    # Создание группы для хранения пуль.
    bullets = Group()
    aliens = Group()
    # Создание пришельца.
    alien = Alien(ai_settings, screen)
    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, aliens, ship.rect.height)  

    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(ai_settings, screen ,ship, bullets)
        ship.update()
        # Удаление пуль, вышедших за край экрана.
        gf.update_bullets(bullets)
        # При каждом проходе цикла перерисовывается экран.
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()

