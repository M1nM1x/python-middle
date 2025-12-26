import pygame
import SoundController
import color
import consts
from Fruit import Fruit
from RenderEngine import RenderEngine
from Snake import Snake


class SnakeGame:
    def __init__(self):
        pygame.init()
        SoundController.main_music.play(-1)
        self.render = RenderEngine()
        self.clock = pygame.time.Clock()
        self.game_over = False

        self.snake = Snake(color.black, 10)
        self.fruit = None

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            elif event.type == pygame.KEYDOWN:
                # TODO: реализовать управление змейкой
                pass

    def game_logic(self):
        # TODO: создать фрукт, если его нет
        pass

        self.event_handler()

        # TODO: обработать поедание фрукта
        pass

        self.snake.update()

        # TODO: проверить столкновение со стеной
        pass

        self.clock.tick(consts.game_FPS)

    def game_loop(self):
        while not self.game_over:
            self.game_logic()
            self.render.add_render_object(self.fruit, self.snake)
            self.render.render()

        pygame.quit()
        quit()
