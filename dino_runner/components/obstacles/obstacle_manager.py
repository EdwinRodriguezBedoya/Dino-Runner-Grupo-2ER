import pygame
from random import randint
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
    def obsta_alea(self):
        object_ran = randint(0,2)
        if object_ran == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))
        elif object_ran == 1:
            self.obstacles.append(Cactus(LARGE_CACTUS))
        else:
            self.obstacles.append(Bird(BIRD))
                
    def update(self, game):
        if len(self.obstacles) == 0:
            self.obsta_alea()
   
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if obstacle.rect.colliderect(game.player.rect):
                pygame.time.delay(500)
                game.playing = False
                game.death_count += 1
 
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            
    def reset_obstacles(self):
        self.obstacles = []

 
