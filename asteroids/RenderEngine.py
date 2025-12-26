import pygame
import sprites
import consts


class RenderEngine:
    def __init__(self):
        # TODO: создать экран игры
        self.screen = None

        pygame.display.set_caption(consts.game_title)

        # TODO: получить rect фона
        self.background_rect = None

        self.render_queue_list = []

        pygame.font.init()
        self.font = pygame.font.Font(None, 36)

    def render_frame(self, lives, score):
        # TODO: отрисовать фон
        pass

        self.__render_queue()

        # Отображение жизней
        lives_text = self.font.render(f"Lives: {lives}", True, (0, 0, 0))
        self.screen.blit(lives_text, (10, 10))

        # Отображение очков
        score_text = self.font.render(f"Score: {score}", True, (0, 0, 0))
        self.screen.blit(score_text, (10, 50))

        # TODO: обновить экран
        pass

    def __render_queue(self):
        for render_object in self.render_queue_list:
            render_object.draw(self.screen)
        self.render_queue_list.clear()

    def add_render_object(self, *renders_object):
        # TODO: добавить объекты в очередь отрисовки
        pass
