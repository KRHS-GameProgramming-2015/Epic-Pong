import sys, pygame, math 
from ball import Ball

class Score():
    def __init__(self, pos = [0,0]):
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.image = self.font.render(str(self.score), 1, (0, 0, 0))
        self.rect = self.image.get_rect(center = pos)
        
    def update():
        self.image = self.font.render(str(self.score), 1, (0, 0, 0))
        self.rect = self.image.get_rect(center = self.rect.center)
        
    
    def increase(self, amount=0):
        self.score += amount
    
    def decrease(self, amount=0):
        self.score -= amount
        
    def reset(self, amount=0):
        self.score = amount
