import images
import pygame
from constants import SelectCharacter as C

class SelectCharacter:
    def __init__(self, screen, gameStateManager, characterManager):
        '''initialize select character screen'''
        self.screen = screen
        self.gameStateManager = gameStateManager
        self.characterManager = characterManager

        #background image
        self.background = images.SelectCharacter.background

        #arrows
        self.left_arrow = images.SelectCharacter.left_arrow
        self.right_arrow = images.SelectCharacter.right_arrow
        self.left_arrow_rect = self.left_arrow.get_rect()
        self.right_arrow_rect = self.right_arrow.get_rect()
        self.left_arrow_rect.center = C.left_arrow_pos
        self.right_arrow_rect.center = C.right_arrow_pos

        #select button
        self.select = images.SelectCharacter.select
        self.select_rect = self.select.get_rect()
        self.select_rect.center = C.select_pos


        self.characterrect = pygame.Rect(0,0,256,384)
        self.characterrect.center = C.character_pos
        
        self.character_list = [
            ['Liam',images.Characters.Liam],
            ['Ben',images.Characters.Ben],
            ['Ethan',images.Characters.Ethan],
            ['James',images.Characters.James],
            ['Mason',images.Characters.Mason],
            ['Noah',images.Characters.Noah],
            ['Oliver',images.Characters.Oliver],
            ['Will',images.Characters.Will],
            ['Amy', images.Characters.Amy],
            ['Ava', images.Characters.Ava],
            ['Emma', images.Characters.Emma],
            ['Izzy', images.Characters.Izzy],
            ['Mia', images.Characters.Mia],
            ['Olivia', images.Characters.Olivia],
            ['Sophia', images.Characters.Sophia],
            ['Zoe', images.Characters.Zoe],]
        
        self.current_character_idx = 0
        
    def run(self, events):
        '''Run select character screen'''
        # Blit the background onto the screen
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                #check if mouse is in button area
                if self.right_arrow_rect.collidepoint(event.pos):
                    self.right_arrow = images.SelectCharacter.right_arrow_scaled
                    self.right_arrow_rect = images.SelectCharacter.right_arrow_scaled.get_rect()
                elif self.left_arrow_rect.collidepoint(event.pos):
                    self.left_arrow = images.SelectCharacter.left_arrow_scaled
                    self.left_arrow_rect = images.SelectCharacter.left_arrow_scaled.get_rect()
                elif self.select_rect.collidepoint(event.pos):
                    self.select = images.SelectCharacter.select_scaled
                    self.select_rect = images.SelectCharacter.select_scaled.get_rect()
                else:
                    self.left_arrow = images.SelectCharacter.left_arrow
                    self.left_arrow_rect = images.SelectCharacter.left_arrow.get_rect()
                    self.right_arrow = images.SelectCharacter.right_arrow
                    self.right_arrow_rect = images.SelectCharacter.right_arrow.get_rect()
                    self.select = images.SelectCharacter.select
                    self.select_rect = images.SelectCharacter.select.get_rect()
                self.left_arrow_rect.center = C.left_arrow_pos
                self.right_arrow_rect.center = C.right_arrow_pos
                self.select_rect.center = C.select_pos
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.right_arrow_rect.collidepoint(event.pos):
                    self.current_character_idx = (self.current_character_idx + 1) % len(self.character_list)
                if self.left_arrow_rect.collidepoint(event.pos):
                    self.current_character_idx = (self.current_character_idx - 1) % len(self.character_list)
                if self.select_rect.collidepoint(event.pos):
                    self.characterManager.setMainCharacter(self.character_list[self.current_character_idx][0])

        self.screen.blit(self.background, (0, 0))

        self.screen.blit(self.left_arrow, self.left_arrow_rect)
        self.screen.blit(self.right_arrow, self.right_arrow_rect)

        self.screen.blit(self.select, self.select_rect)

        self.screen.blit(self.character_list[self.current_character_idx][1], self.characterrect)

