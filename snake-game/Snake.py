import pygame
import copy
from CollidableObject import CollidableObject
from RenderObject import RenderObject


class Snake(CollidableObject, RenderObject):
    def __init__(self, color, block_size):
        self.color = color
        self.block_size = block_size
        self.snake_list = []
        self.snake_length = 1
        self.vector_x = 0
        self.vector_y = 0
        self.speed = 10

        # Начальная позиция головы
        self.head = pygame.Rect(200, 200, block_size, block_size)

    def move(self, x_change, y_change):
        # TODO: изменить вектор движения змейки
        pass

    def update(self):
        # TODO: переместить голову змейки
        pass

        # TODO: обновить rect для столкновений
        pass

        # TODO: добавить новый сегмент в snake_list
        pass

        # TODO: удалить лишние сегменты
        pass

    def draw(self, surface):
        for part in self.snake_list:
            pygame.draw.rect(surface, self.color, part)

    def eat(self):
        # TODO: увеличить длину змейки
        pass
