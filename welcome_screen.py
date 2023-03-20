# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 09:50:38 2023

@author: parita, roshan, rintu
"""

import screen as s
import pygame

class Welcome_Screen(s.Screen):
        
    pygame.init()
    wlcm_scrn = pygame.display.set_mode((500,700))
    pygame.display.set_caption(s.Screen.title)
    #pygame.display.set_icon(s.Screen.icon)
    
    
class Button(Welcome_Screen):
    
    def __init__(self,x,y,img,scale):
        self.x_pos = x
        self.y_pos = y

        #Resizing the image of Button
        w = img.get_width()
        h = img.get_height()
        self.image = pygame.transform.scale(img,(int(w*scale),int(h*scale)))
        self.btn_rect = self.image.get_rect(center=(self.x_pos,self.y_pos))
        
        #Adding Text to the button
        #self.text_input = text_input
        #self.text = Welcome_Screen.main_font.render(self.text_input, True, (255,255,255))
        #self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def draw_btn(self):
        Welcome_Screen.wlcm_scrn.blit(self.image, self.btn_rect)
        #Welcome_Screen.wlcm_scrn.blit(self.text,self.text_rect)
           
    def checkIp(self,position):
        if position[0] in range(self.btn_rect.left, self.btn_rect.right) and position[1] in range(self.btn_rect.top, self.btn_rect.bottom):
            return True