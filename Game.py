# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 12:54:02 2023

@author: parita, rintu, roshan
"""

import screen as s
import pygame
#from pygame import mixer
import welcome_screen as w

import Level1_map as l1
import Level2_map as l2
import Level 
import dialogueBox as db


FramePerSec = pygame.time.Clock()
FPS = 180
# background_sprite = pygame.image.load('./Images/background.png')
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
            w.Welcome_Screen.wlcm_scrn.fill((18,18,18))
            button_start.draw_btn_welcome()
            button_exit.draw_btn_welcome()
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
        #Dialogu box before level 1
        s.Screen.scrn.fill((106, 159, 181))
        dialogue_box = db.Dialogue(100, 100, 600, 100, text_speed=50)
        dialogue_box.display("Hello! How are you?")
        pygame.time.delay(5000)  # wait for 2 seconds
        dialogue_box.display("Great, thanks for asking")
        pygame.time.delay(2000)
        
        #Level 1 implementation
        level = Level.Level(l1.level_map,s.Screen.scrn)
        
        while running:
            clock.tick(180)
            #pygame.display.flip()
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            s.Screen.scrn.fill((106, 159, 181))
            level.run()

            pygame.display.update()
            s.Screen.clock.tick(180)
            FramePerSec.tick(FPS)

        pygame.quit()