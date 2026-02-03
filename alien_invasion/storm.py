#12-2 Game Character
import pygame
from settings import Settings
class Storm:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        self.image = pygame.image.load('images/storm.bmp')
        self.settings = Settings()
        
        self.image.set_colorkey(self.settings.bg_color) 
        self.rect = self.image.get_rect()
        
        self.rect.center = self.screen_rect.center
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)