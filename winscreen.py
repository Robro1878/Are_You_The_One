import images
import pygame
from constants import WinScreen as C

class WinScreen:
    def __init__(self, screen, gameStateManager, characterManager):
        '''Initializes start screen'''
        self.screen = screen
        self.gameStateManager = gameStateManager
        self.character_manager = characterManager
        self.background = images.WinScreen.background
        self.back_button = images.LoseScreen.back_button
        self.back_button_rect = self.back_button.get_rect()
        self.back_button_rect.center = C.back_button_pos
        self.maincharacter_image = None
        self.maincharacter_rect = None
        self.correctcharacter_image = None
        self.correctcharacter_rect = None
    
    

    def run(self, events):
        '''Runs start screen'''
        if self.maincharacter_image is None:
            self.maincharacter_image = images.Characters.character_dict[self.character_manager.getMainCharacter()]
            self.maincharacter_rect = self.maincharacter_image.get_rect()
            self.maincharacter_rect.center = C.main_character_pos
        if self.correctcharacter_image is None:
            self.correctcharacter_image = images.Characters.character_dict[self.character_manager.getMatch()]
            self.correctcharacter_rect = self.correctcharacter_image.get_rect()
            self.correctcharacter_rect.center = C.match_pos
        
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                if self.back_button_rect.collidepoint(event.pos):
                    self.back_button = images.WinScreen.back_button_scaled
                    self.back_button_rect = images.WinScreen.back_button_scaled.get_rect()
                else:
                    self.back_button = images.WinScreen.back_button
                    self.back_button_rect = self.back_button.get_rect()
                self.back_button_rect.center = C.back_button_pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button_rect.collidepoint(event.pos):
                    self.gameStateManager.setState("messenger")
        
        # Blit the background onto the screen
        self.screen.blit(self.background, (0,0))

        #Blit characters on to screen
        self.screen.blit(self.maincharacter_image, self.maincharacter_rect)
        self.screen.blit(self.correctcharacter_image, self.correctcharacter_rect)
        self.screen.blit(self.back_button, self.back_button_rect)


