import pygame
import constants

class Message:
    def __init__(self, screen, text:str, user:bool):
        self.screen = screen
        self.text = text
        self.font = pygame.font.SysFont(None, 30)
        self.user = user
        if not self.user:
            self.left = 162
        else:
            self.left = constants.game.screen_width - (len(self.text) * 13) - 12
        self.rect = pygame.Rect(self.left, 0, len(self.text) * 13, constants.Messaging.message_height)
    
    def run(self):
        if self.user:
            color = constants.Colors.BLUE
        else:
            color = constants.Colors.BLACK
        pygame.draw.rect(self.screen, color, self.rect, 2)
        text = self.font.render(self.text, True, constants.Colors.BLACK)
        self.screen.blit(text, self.rect.move(5,5))
    
    def setHeight(self, height):
        self.rect.top = height




