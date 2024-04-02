import pygame
import sys

class Text_Input_Field:
    def __init__(self, screen, fontsize:int, rect:pygame.Rect):
        self.font = pygame.font.SysFont(None, fontsize)
        self.rect = rect
        self.screen = screen

        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (200, 200, 200)

        # Text input field
        self.text = ""
        self.active = False
    
    def run(self, events):

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.active = not self.active
                else:
                    self.active = False
            elif event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode

        # Fill the screen
        # Draw text input field
        pygame.draw.rect(self.screen, self.GRAY, self.rect)
        pygame.draw.rect(self.screen, self.BLACK, self.rect, 2)
        input_text = self.font.render(self.text, True, self.BLACK)
        self.screen.blit(input_text, self.rect.move(5, 5))

    def get_input(self):
        return self.text
