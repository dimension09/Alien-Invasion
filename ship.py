import pygame

class Ship ():

    def __init__(self, ai_settings, screen):
        # Инициализирует корабль и задает его начальную позицию.
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения корабля и получение прямоугольника.

        self.image = pygame.image.load('images/slip.png') # Загрузка изображения
        self.rect = self.image.get_rect() #  метод get_rect() используется для получения атрибута rect, задает текущую позицию прямоугольника
        self.screen_rect = screen.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx # Местонахождение центра игрового элемента определяется атрибутами center, centerx или centery прямоугольника
        self.rect.bottom = self.screen_rect.bottom
        # Сохранение вещественной координаты центра корабля.
        self.center = float(self.rect.centerx)
        # Флаг перемещения.
        self.moving_right = False
        self.moving_left = False


    def update (self):
        # Обновляет позицию корабля с учетом флага.
        # Обновляется атрибут center, не rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # Обновление атрибута rect на основании self.center.
        self.rect.centerx = self.center

    def blitme (self):
        # Рисует корабль в текущей позиции.
        self.screen.blit(self.image, self.rect) #  blitme(), который выводит изображение на экран в позиции, заданной self.rect.
