import sys
import pygame
from constants import game as C
from startscreen import StartScreen
from select_character import SelectCharacter
from CharacterManager import CharacterManager
from select_preferences import SelectPreferences
from messenger import Messenger
from winscreen import WinScreen
from losescreen import LoseScreen

class Game:
    def __init__(self):
        '''Initializes game'''
        pygame.init()

        self.screen = pygame.display.set_mode((C.screen_width, C.screen_height))
        pygame.display.set_caption(C.window_title) #Window title
        self.clock = pygame.time.Clock()

        self.gameStateManager = GameStateManager('start')
        self.characterManager = CharacterManager(C.characters)
        self.startscreen = StartScreen(self.screen, self.gameStateManager)
        self.select_character = SelectCharacter(self.screen, self.gameStateManager, self.characterManager)
        self.select_preferences = SelectPreferences(self.screen, self.gameStateManager, self.characterManager)
        self.messenger = Messenger(self.screen, self.gameStateManager, self.characterManager)
        self.winscreen = WinScreen(self.screen, self.gameStateManager, self.characterManager)
        self.losescreen = LoseScreen(self.screen, self.gameStateManager, self.characterManager)

        self.states = {
            'start': self.startscreen, 
            'select_character': self.select_character, 
            'select_preferences': self.select_preferences, 
            'messenger': self.messenger,
            'winscreen': self.winscreen,
            'losescreen': self.losescreen}

    def run(self):
        '''Runs game'''
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.states[self.gameStateManager.getState()].run(events)


            # Update the display
            pygame.display.flip()
            self.clock.tick(C.fps)

class GameStateManager:
    def __init__(self, current_state):
        #initialize states
        
        self.current_state = current_state
    
    def getState(self):
        return self.current_state
    def setState(self, state):
        self.current_state = state


game = Game()
game.run()

