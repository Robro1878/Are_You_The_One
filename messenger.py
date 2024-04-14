from messaging_select import Messaging_Select
from constants import game
import pygame
from character_messenging import Character_Messenging

class Messenger:
    def __init__(self, screen, gamestatemanager, characterManager):
        self.screen = screen
        self.gameStateManager = gamestatemanager
        self.characterManager = characterManager
        self.messaging_selects = []
        self.stateManager = StateManager()
        self.states = {'select_character': Character_Messenging(self.screen, None, self.characterManager)}

        self.scroll_y = 0
        self.scroll_speed = 30


    def run(self, events):
        if self.messaging_selects == []:
            for character in self.characterManager.getOtherCharacters():
                self.messaging_selects.append(Messaging_Select(self.screen, character, self.characterManager))
                self.states[character] = Character_Messenging(self.screen, character, self.characterManager)
            for i in range(len(self.characterManager.getOtherCharacters())):
                self.messaging_selects[i].setLocation(i * game.screen_height//len(self.characterManager.getOtherCharacters()))

        for select in self.messaging_selects:
            select.run()

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    for select in self.messaging_selects:
                        if select.getRect().collidepoint(event.pos):
                            #if users clicks on one of the characters, we need to make sure none of the other characters are active and then set the new character active
                            for select_unactivate in self.messaging_selects:
                                select_unactivate.setActive(False)
                            
                            self.stateManager.setState(select.getCharacter())
                            select.setActive(True)
                            self.scroll_y = 0
                
                if event.button == pygame.BUTTON_WHEELDOWN and self.scroll_y > 0:
                    self.scroll_y -= self.scroll_speed
                
                if event.button == pygame.BUTTON_WHEELUP:
                    self.scroll_y +=  self.scroll_speed
                    
        self.states[self.stateManager.getState()].run(events, self.scroll_y)            


class StateManager:
    def __init__(self):
        self.state = 'select_character'
    
    def setState(self, state):
        self.state = state
    
    def getState(self):
        return self.state
    
