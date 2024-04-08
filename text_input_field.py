import pygame
from constants import Colors

class Text_Input_Field:
    def __init__(self, screen, fontsize:int, rect:pygame.Rect):
        self.font = pygame.font.SysFont(None, fontsize)
        self.rect = rect
        self.screen = screen



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
        pygame.draw.rect(self.screen, Colors.GRAY, self.rect)
        if self.active:
            pygame.draw.rect(self.screen, Colors.BLUE, self.rect, 4)
        else: 
            pygame.draw.rect(self.screen, Colors.BLACK, self.rect, 2)
        
        input_text = self.font.render(self.text, True, Colors.BLACK)
        self.screen.blit(input_text, self.rect.move(5, 5))

    def get_input(self):
        return self.text
    
    def reset(self):
        self.text = ""
