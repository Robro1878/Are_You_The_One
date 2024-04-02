from text_input_field import Text_Input_Field
import images
import pygame
from constants import SelectPreferences as C
from constants import Colors


class SelectPreferences:
    def __init__(self, screen, gameStateManager, characterManager):
        self.screen = screen
        self.gameStateManager = gameStateManager
        self.characterManager = characterManager
        self.interests_input = Text_Input_Field(self.screen, 30, C.interests_input_rect)
        self.job_input = Text_Input_Field(self.screen, 30, C.job_input_rect)
        self.values_input = Text_Input_Field(self.screen, 30, C.values_input_rect)
        self.text_inputs = [self.interests_input,self.job_input,self.values_input]
        self.background = images.SelectPreferences.background
        
        self.male_symbol = images.SelectPreferences.male_symbol
        self.female_symbol = images.SelectPreferences.female_symbol
        self.male_symbol_rect = self.male_symbol.get_rect()
        self.female_symbol_rect = self.female_symbol.get_rect()
        self.male_symbol_rect.center = C.male_symbol_pos
        self.female_symbol_rect.center = C.female_symbol_pos

        self.selected_gender = None

    def run(self, events):

        for event in events:
            if event.type == pygame.MOUSEMOTION:
                #check if mouse is in button area
                if self.male_symbol_rect.collidepoint(event.pos):
                    self.male_symbol = images.SelectPreferences.male_symbol_scaled
                    self.male_symbol_rect = images.SelectPreferences.male_symbol_scaled.get_rect()
                elif self.female_symbol_rect.collidepoint(event.pos):
                    self.female_symbol = images.SelectPreferences.female_symbol_scaled
                    self.female_symbol_rect = images.SelectPreferences.female_symbol_scaled.get_rect()
                else:
                    self.female_symbol = images.SelectPreferences.female_symbol
                    self.female_symbol_rect = images.SelectPreferences.female_symbol.get_rect()
                    self.male_symbol = images.SelectPreferences.male_symbol
                    self.male_symbol_rect = images.SelectPreferences.male_symbol.get_rect()
                self.female_symbol_rect.center = C.female_symbol_pos
                self.male_symbol_rect.center = C.male_symbol_pos
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.male_symbol_rect.collidepoint(event.pos):
                    self.selected_gender = 'Male'
                if self.female_symbol_rect.collidepoint(event.pos):
                    self.selected_gender = 'Female'
        


        self.screen.blit(self.background, (0,0))
        for text_input in self.text_inputs:
            text_input.run(events)
        
        self.screen.blit(self.female_symbol, self.female_symbol_rect)
        self.screen.blit(self.male_symbol, self.male_symbol_rect)

        if self.selected_gender == 'Male':
            pygame.draw.rect(self.screen, Colors.green, self.male_symbol_rect, 3, 3)
        elif self.selected_gender == 'Female':
            pygame.draw.rect(self.screen, Colors.green, self.female_symbol_rect, 3, 3)