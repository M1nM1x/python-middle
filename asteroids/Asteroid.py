import pygame
import consts
import sprites
from CollidableObject import CollidableObject
from RendarableObject import RendarableObject
import random


class Asteroid(RendarableObject, CollidableObject):
    def __init__(self, speed):
        # TODO: определить, хороший ли астероид
        self.is_good = None

        # TODO: выбрать изображение
        self.image = None

        self.height = 60 + random.randint(-5, 5)
        self.width = 63 + random.randint(-5, 5)

        # TODO: масштабировать изображение
        pass

        # TODO: создать rect астероида
        self.rect = None

        # TODO: задать начальные координаты
        pass

        # TODO: вычислить скорость
        self.speed = None

    def move(self):
        # TODO: движение астероида влево
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)
