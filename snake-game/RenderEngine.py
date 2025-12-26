import pygame
import color
import consts


class RenderEngine:
    def __init__(self):
        # TODO: создать окно pygame с параметрами экрана
        self.surface = None

        # Очередь объектов для отрисовки
        self.render_queue = []

    def render(self):
        # TODO: залить экран фоновым цветом
        pass

        # TODO: отрисовать все объекты из очереди
        for render_object in self.render_queue:
            pass

        # TODO: обновить экран
        pass

        # TODO: очистить очередь отрисовки
        pass

    def add_render_object(self, *renders_object):
        # TODO: добавить все объекты в очередь отрисовки
        pass
