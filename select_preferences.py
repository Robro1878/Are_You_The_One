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

        self.next_button = images.SelectPreferences.next_button
        self.next_button_rect = self.next_button.get_rect()
        self.next_button_rect.center = C.next_button_pos

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
                elif self.next_button_rect.collidepoint(event.pos):
                    self.next_button = images.SelectPreferences.next_button_scaled
                    self.next_button_rect = images.SelectPreferences.next_button_scaled.get_rect()
                else:
                    self.female_symbol = images.SelectPreferences.female_symbol
                    self.female_symbol_rect = images.SelectPreferences.female_symbol.get_rect()
                    self.male_symbol = images.SelectPreferences.male_symbol
                    self.male_symbol_rect = images.SelectPreferences.male_symbol.get_rect()
                    self.next_button = images.SelectPreferences.next_button
                    self.next_button_rect = images.SelectPreferences.next_button.get_rect()
                self.female_symbol_rect.center = C.female_symbol_pos
                self.male_symbol_rect.center = C.male_symbol_pos
                self.next_button_rect.center = C.next_button_pos
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.male_symbol_rect.collidepoint(event.pos):
                    self.selected_gender = 'Male'
                if self.female_symbol_rect.collidepoint(event.pos):
                    self.selected_gender = 'Female'
                if self.next_button_rect.collidepoint(event.pos):
                    self.characterManager.setGender_Preference(self.selected_gender)
                    self.characterManager.setInterest_Preference(self.interests_input.get_input())
                    self.characterManager.setJob_Preference(self.job_input.get_input())
                    self.characterManager.setValues_Preference(self.values_input.get_input())
                    self.characterManager.randomizeOtherPlayerTraits()
                    self.characterManager.create_chatbots()
                    self.gameStateManager.setState('messenger')


        self.screen.blit(self.background, (0,0))
        for text_input in self.text_inputs:
            text_input.run(events)
        
        self.screen.blit(self.female_symbol, self.female_symbol_rect)
        self.screen.blit(self.male_symbol, self.male_symbol_rect)

        self.screen.blit(self.next_button,self.next_button_rect)

        if self.selected_gender == 'Male':
            pygame.draw.rect(self.screen, Colors.GREEN, self.male_symbol_rect, 3, 3)
        elif self.selected_gender == 'Female':
            pygame.draw.rect(self.screen, Colors.GREEN, self.female_symbol_rect, 3, 3)