import sys

import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # Реагирует на нажатие клавиш.
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet (ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

# Создание новой пули и включение ее в группу bullets.
def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    # Реагирует на отпускание клавиш.
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events (ai_settings, screen, ship, bullets):
    for event in pygame.event.get(): # Чтобы получить доступ к событиям, обнаруженным Pygame.
        if event.type == pygame.QUIT:
            sys.exit() # sys завершает игру по команде игрока.
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, aliens, bullets):
    # Обновляет изображения на экране и отображает новый экран.
    # При каждом проходе цикла перерисовывается экран.
    background = pygame.image.load("images/galakt.jpg").convert()
    screen.blit(background, [0, 0]) # экран заполняется фоном

    # Все пули выводятся позади изображений корабля и пришельцев.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Отображение последнего прорисованного экрана.
    pygame.display.flip()

# Обновляет позиции пуль и уничтожает старые пули.
def update_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # Обновление позиций пуль. 
    bullets.update()

def get_number_aliens_x(ai_settings, alien_width):
    # Интервал между соседними пришельцами равен одной ширине пришельца.
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    # Определяет количество рядов, помещающихся на экране.
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number):
    # Создает пришельца и размещает его в ряду.
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien) 

def create_fleet(ai_settings, screen, aliens):
    # Создает флот пришельцев.
    # Создание пришельца и вычисление количества пришельцев в ряду.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Создание первого ряда пришельцев.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

