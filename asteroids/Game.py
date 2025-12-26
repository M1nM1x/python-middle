import pygame
import consts
from Asteroid import Asteroid
from Player import Player
from RenderEngine import RenderEngine
from PhysicEngine import PhysicEngine
from ScoreController import ScoreController


class Game:
    def __init__(self):
        self.render_engine = RenderEngine()
        self.player = Player(150, 150)
        self.score_count = ScoreController()
        self.clock = pygame.time.Clock()
        self.is_end = False

        self.asteroids = []
        self.asteroid_speed = 9
        self.asteroid_speed_ax = 0.01
        self.asteroid_spawn_rate = 1
        self.tick_count = 0

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_end = True

    def game_logic(self):
        # TODO: логика спавна астероидов
        pass

        # TODO: движение астероидов и столкновения
        pass

        keys = pygame.key.get_pressed()

        # TODO: управление игроком
        pass

        # TODO: проверка смерти игрока
        pass

    def main_loop(self):
        self.tick_count = 120

        while not self.is_end:
            self.event_handler()
            self.game_logic()

            self.render_engine.add_render_object(self.player, *self.asteroids)
            self.render_engine.render_frame(
                self.player.lives,
                self.score_count.score
            )

            self.clock.tick(consts.game_FPS)
            self.tick_count += 1

        pygame.quit()
