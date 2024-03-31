import images
from constants import StartScreen as C
import pygame

class StartScreen:
    def __init__(self, screen, gameStateManager):
        '''Initializes start screen'''
        self.screen = screen
        self.gameStateManager = gameStateManager
        #start button config
        self.start_button_rect = images.StartScreen.start_button.get_rect()
        self.start_button_rect.center = C.start_button_pos
        self.start_button_image = images.StartScreen.start_button

        #background image
        self.background = images.StartScreen.start_screen
    
    
    def run(self, events):
        '''Runs start screen'''
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                #check if mouse is in button area
                if self.start_button_rect.collidepoint(event.pos):
                    self.start_button_image = images.StartScreen.start_button_scaled
                    self.start_button_rect = images.StartScreen.start_button_scaled.get_rect()
                else:
                    self.start_button_image = images.StartScreen.start_button
                    self.start_button_rect = images.StartScreen.start_button.get_rect()
                self.start_button_rect.center = C.start_button_pos
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click is within the button area
                if self.start_button_rect.collidepoint(event.pos):
                    self.gameStateManager.setState('select_character')

        # Blit the background onto the screen
        self.screen.blit(self.background, (0, 0))

        #Blit the start button onto the screen
        self.screen.blit(self.start_button_image, self.start_button_rect)


