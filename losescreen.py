import images
import pygame
from constants import LoseScreen as C

class LoseScreen:
    def __init__(self, screen, game_state_manager, character_manager):
        self.screen = screen
        self.game_state_manager = game_state_manager
        self.character_manager = character_manager
        self.background = images.LoseScreen.background
        self.back_button = images.LoseScreen.back_button
        self.back_button_rect = self.back_button.get_rect()
        self.back_button_rect.center = C.back_button_pos

        self.maincharacter_image = None
        self.maincharacter_rect = None
        self.incorrectcharacter_image = None
        self.incorrectcharacter_rect = None

    def run(self, events):
        if self.maincharacter_image is None:
            self.maincharacter_image = images.Characters.character_dict[self.character_manager.getMainCharacter()]
            self.maincharacter_rect = self.maincharacter_image.get_rect()
            self.maincharacter_rect.center = C.main_character_pos

        self.incorrectcharacter_image = images.Characters.character_dict[self.character_manager.getSelectedCharacter()]
        self.incorrectcharacter_rect = self.incorrectcharacter_image.get_rect()
        self.incorrectcharacter_rect.center = C.incorrect_match_pos
        
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                if self.back_button_rect.collidepoint(event.pos):
                    self.back_button = images.LoseScreen.back_button_scaled
                    self.back_button_rect = images.LoseScreen.back_button_scaled.get_rect()
                else:
                    self.back_button = images.LoseScreen.back_button
                    self.back_button_rect = self.back_button.get_rect()
                self.back_button_rect.center = C.back_button_pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button_rect.collidepoint(event.pos):
                    self.game_state_manager.setState("messenger")
                # Blit the background onto the screen
        self.screen.blit(self.background, (0,0))

        #Blit characters on to screen
        self.screen.blit(self.maincharacter_image, self.maincharacter_rect)
        self.screen.blit(self.incorrectcharacter_image, self.incorrectcharacter_rect)
        self.screen.blit(self.back_button, self.back_button_rect)
        
