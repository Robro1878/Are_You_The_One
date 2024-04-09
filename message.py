import pygame
import constants

class Message:
    def __init__(self, screen, text:str, user:bool):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 30)
        self.text = self.font.render(text,True, constants.Colors.BLACK)
        self.rect = self.text.get_rect()
        self.user = user
        if not self.user:
            self.left = 162
        else:
            self.left = constants.game.screen_width - self.rect.width - 12
        self.rect.topleft = self.left,constants.Messaging.message_initial_height
        self.rect.height = constants.Messaging.message_height
        self.rect.width += 10
    
    def run(self):
        if self.user:
            color = constants.Colors.BLUE
        else:
            color = constants.Colors.BLACK

        self.rect.top = self.height
        self.screen.blit(self.text, self.rect.move(5,5))
        pygame.draw.rect(self.screen, color, self.rect, 2)

    def setHeight(self, height):
        self.height = height




