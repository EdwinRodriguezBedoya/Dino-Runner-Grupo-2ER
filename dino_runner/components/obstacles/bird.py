from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD
from random import randint

class Bird(Obstacle):
    def __init__(self, image):
        super().__init__(image[0])
        self.rect.y = randint(200, 300)
        self.step = 0
    
    
        
    def draw (self, screen):
        if self.step >= 9:
            self.step = 0
        self.step += 1
        screen.blit(BIRD[self.step//5], self.rect)
        