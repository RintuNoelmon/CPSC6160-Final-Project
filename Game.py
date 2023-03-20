# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 12:54:02 2023

@author: parita, rintu, roshan
"""

import screen as s
import pygame
#from pygame import mixer
import welcome_screen as w



class Game(s.Screen):
    def run(self):
        running = False
        #game_over = False
        welcome_screen = True
        #mixer.music.load(r"Music/bgMusic.wav")
        #mixer.music.play(-1)

        #Welcome Screen 
        
        
        button_img_start = pygame.image.load("Images/button.png").convert_alpha()
        button_start = w.Button(250,300,button_img_start,0.7)
        button_img_exit = pygame.image.load("Images/button_exit.png").convert_alpha()  
        button_exit = w.Button(250,450,button_img_exit,0.76)

        while welcome_screen == True:
            w.Welcome_Screen.wlcm_scrn.fill((106, 159, 181))
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
                        break
                    if btn_exit == True:
                        pygame.quit()
                        #pygame.display.flip()
            pygame.display.flip()
            s.Screen.clock.tick(360)

        #Main Screen
        while running:
            s.Screen.scrn.fill((106, 159, 181))
            #pygame.display.flip()
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                running=False
                
                
            pygame.display.flip()
            s.Screen.clock.tick(360)

        pygame.quit()