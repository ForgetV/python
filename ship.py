import pygame


class Ship():
    def __init__(self,ai_settings,screen):
        self.screen=screen

        self.ai_settings=ai_settings

        self.image=pygame.image.load("/usr/python/business/AlienGame/images/ship.bmp")
        self.rect=self.image.get_rect()
        self.height=self.rect.right-self.rect.left
        self.screen_rect=screen.get_rect()

        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        self.centerx=float(self.rect.centerx)
        self.centery=float(self.rect.bottom)

        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False

    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.centerx+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.bottom>self.height:
            self.centery -= self.ai_settings.ship_speed_factor
            print self.rect.bottom
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.centery +=  self.ai_settings.ship_speed_factor
        self.rect.centerx=self.centerx
        self.rect.bottom=self.centery

    def biltme(self):
        self.screen.blit(self.image,self.rect)