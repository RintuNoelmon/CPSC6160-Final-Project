# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 12:54:02 2023

@author: parita, rintu, roshan
"""

import screen as s
import pygame
#from pygame import mixer
import welcome_screen as w
from Level2 import Level2

from settings import *


FramePerSec = pygame.time.Clock()
FPS = 180
background_sprite = pygame.image.load('./Images/img.png')
class Game(s.Screen):
    def run(self):
        running = False
        #game_over = False
        clock = pygame.time.Clock()

        welcome_screen = True
        #mixer.music.load(r"Music/bgMusic.wav")
        #mixer.music.play(-1)

        #Welcome Screen 
        # self.image = background_sprite
        button_img_start = pygame.image.load("Images/button.png").convert_alpha()
        button_start = w.Button(600,300,button_img_start,0.7)
        button_img_exit = pygame.image.load("Images/button_exit.png").convert_alpha()  
        button_exit = w.Button(600,450,button_img_exit,0.76)

        while welcome_screen == True:
            w.Welcome_Screen.wlcm_scrn.fill((202, 228, 241))
            button_start.draw_btn()
            button_exit.draw_btn()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    welcome_screen = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    btn_start = button_start.checkIp(pygame.mouse.get_pos())
                    btn_exit = button_exit.checkIp(pygame.mouse.get_pos())
                    if btn_start == True:
                        welcome_screen = False
                        running = True


                    if btn_exit == True:
                        pygame.quit()
                        #pygame.display.flip()
            pygame.display.flip()
            s.Screen.clock.tick(3600)

        #Main Screen
        # test_tile=pygame.sprite.Group(Tile((100,100),200))
        level = Level2(level_map,s.Screen.scrn)
        window = pygame.display.set_mode((1200, 700))
        bg = pygame.transform.scale(background_sprite, (1200, 700))
        i=0
        while True:
            clock.tick(180)
            window.fill((0, 0, 0))
            window.blit(bg, (i, 0))
            window.blit(bg, (1200 + i, 0))
            if (i == -1200):
                window.blit(bg, (1200 + i, 0))
                i = 0
            i -= 1
            # pygame.display.flip()
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                running=True

            # s.Screen.scrn.fill((106, 159, 181))
            # s.Screen.scrn.blits(background_sprite, (1200,700))
            level.run()

            pygame.display.update()
            s.Screen.clock.tick(180)
            FramePerSec.tick(FPS)

        pygame.quit()
