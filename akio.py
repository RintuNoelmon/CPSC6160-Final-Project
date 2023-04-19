# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 12:11:06 2023

@author: parita, rintu, roshan
"""

import pygame

from Anime import import_folder
import random

# Initialize pygame
#pygame.init()

# Screen dimensions
# WIDTH = 800
# HEIGHT = 600
#load hero sprite
# hero_sprite = pygame.image.load('./Images/Character/Idle/1.png')
fps = 60
#hero class
class Hero(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.import_character()
        self.frame_index = 0
        self.animation_speed = 0.021
        self.image = self.animations['Idle'][self.frame_index]
        # self.image = pygame.Surface((32, 64))
        # self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)
        self.facing_right = True

        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.05
        self.jump_speed = -4
        self.fall_count = 0
        self.on_ground = False
        self.on_ceiling = False
        self.jumped = False

        # self.image = hero_sprite
        # self.rect = self.image.get_rect()
        # self.rect.x = WIDTH // 2
        # self.rect.y = HEIGHT // 2

    def import_character(self):
        character_path = './Images/Character/'
        self.animations = {'Idle':[],'run':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            print(full_path)
            self.animations[animation] = import_folder(full_path)




    def char_ground(self):
        if self.on_ground:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)
        else:
            self.rect = self.image.get_rect(center=self.rect.center)

    def animate(self):
        animation = self.animations['Idle']

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            facing_left= pygame.transform.flip(image,True,False)
            self.image = facing_left


    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.on_ground and self.jumped == False:
            self.jump()
        if keys[pygame.K_SPACE] == False:
            self.jumped = False

    def get_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.animate()



# pygame.quit()
