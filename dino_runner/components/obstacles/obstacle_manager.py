import pygame
from dino_runner.components.obstacles.cactus import Cactus, CactusLa
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.obstaclesLa = []
        
    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))
            self.obstacles.append(CactusLa(LARGE_CACTUS))
            
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if obstacle.rect.colliderect(game.player.rect):
                pygame.time.delay(2000)
                game.playing = False
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)