import pygame
import sys

from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *


class TextSprite(pygame.sprite.Sprite):
    def __init__(self, size):
        super().__init__()
        self.color = "white"
        self.pos = pygame.Vector2(0,0)
        self.font = pygame.font.Font(None, size)
        self.text = self.font.render("Score: 0",True,self.color)
        self.rect = self.text.get_rect(midtop=(SCREEN_WIDTH // 2, 10))

        


    def update(self, score):
        self.text = self.font.render(f"Score: {score}",True,self.color)

        
        

