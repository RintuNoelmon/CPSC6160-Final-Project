# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 12:11:06 2023

@author: parita, rintu, roshan
"""

import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
#load hero sprite
hero_sprite = pygame.image.load('hero.png')

#hero class
class Hero(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = hero_sprite
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT // 2

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5


pygame.quit()
