import pygame
import SoundController
import color
import consts
from CollidableObject import CollidableObject
from RenderObject import RenderObject
import random


class Fruit(CollidableObject, RenderObject):
    def __init__(self):
        self.color = color.red
        self.width = 15
        self.height = 15

        # TODO: сгенерировать случайные координаты фрукта
        self.x = None
        self.y = None

        # TODO: создать rect фрукта
        self.rect = None

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def destroy(self):
        SoundController.fruit_eat.play()
        del self
