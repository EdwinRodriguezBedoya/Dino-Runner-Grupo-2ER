import pygame
from dino_runner.utils.constants import FONT_STYLE

class Score:
    def __init__(self):
        self.points = 0
    
    def update(self, game):
        self.points += 1
        if self.points % 100 == 0:
            game.game_speed += 2
            
        game.point_act = self.points
    
    def draw(self, screen):
        #poner mensaje de Bienvenida
        font = pygame.font.Font(FONT_STYLE, 30)
        message = font.render(f"Score: {self.points}", True, (0, 0, 0))
        message_rect = message.get_rect()
        message_rect.center = (1000, 30)
        screen.blit(message,message_rect)
        
    def reset_score(self):
        self.points = 0
    
    
        