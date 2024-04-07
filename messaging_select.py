from constants import Messaging_Select as C
from constants import Colors
from constants import game
import pygame

class Messaging_Select:
    def __init__(self, screen, character: str, characterManager):
        self.screen = screen
        self.character = character
        self.height = game.screen_height // len(characterManager.getOtherCharacters())
        self.width = C.width
        self.font = pygame.font.SysFont(None, C.fontsize)
        self.active = False
        
    
    def setLocation(self, loc):
        self.rect = pygame.Rect(0, loc, self.width, self.height)

    def run(self):
        pygame.draw.rect(self.screen, Colors.GRAY,self.rect)
        if self.active:
            pygame.draw.line(self.screen, Colors.BLUE, self.rect.bottomleft, self.rect.bottomright, 6)
            pygame.draw.line(self.screen, Colors.BLUE, self.rect.bottomright, self.rect.topright, 2)
            pygame.draw.line(self.screen, Colors.BLUE, self.rect.topright, self.rect.topleft, 2)
        else:
            pygame.draw.line(self.screen, Colors.BLACK, self.rect.bottomleft, self.rect.bottomright, 6)
            pygame.draw.line(self.screen, Colors.BLACK, self.rect.bottomright, self.rect.topright, 2)
        
        character_text = self.font.render(self.character, True, Colors.BLACK)
        self.screen.blit(character_text, self.rect)

    def setActive(self, active):
        self.active = active
    
    def getRect(self):
        return self.rect
    
    def getCharacter(self):
        return self.character


    