# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 12:11:06 2023

@author: parita, rintu, roshan
"""

import pygame


#Generalized block of screen
class Screen():

    pygame.init()
    
    #Giving the title
    title = "Isekai Chronicles of the Summoned Hero"
    pygame.display.set_caption(title)
    
    #Puttong icon of the game
    #icon = pygame.image.load(r'Images/pong.ico')
    #pygame.display.set_icon(icon)
    
    main_font = pygame.font.SysFont("cambria", 50)

    scrn = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    
    clock = pygame.time.Clock()
        
        
        