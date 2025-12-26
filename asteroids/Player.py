import pygame
import sprites
from CollidableObject import CollidableObject
from RendarableObject import RendarableObject


class Player(CollidableObject, RendarableObject):
    def __init__(self, x, y):
        self.image = sprites.player_image
        self.lives = 3
        self.is_dead = False
        self.speed = 5

        self.height = 30
        self.width = 60

        # TODO: масштабировать изображение
        pass

        # TODO: создать rect игрока
        self.rect = None

        # TODO: задать начальные координаты
        pass

    def move(self, direction):
        # TODO: реализовать движение по направлению
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def damaged(self):
        # TODO: уменьшить количество жизней
        pass
