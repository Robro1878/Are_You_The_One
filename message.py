import pygame
import constants

class Message:
    def __init__(self, screen, text:str, user:bool):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 30)
        # self.text = self.font.render(text,True, constants.Colors.BLACK)
        self.text = text
        # self.rect = self.text.get_rect()
        self.user = user
        self.left = 162
        self.height = constants.Messaging.message_initial_height
        self.total_text_height = 0
        # if not self.user:
        #     self.left = 162
        # else:
        #     self.left = constants.game.screen_width - self.rect.width - 12
        # self.rect.topleft = self.left,constants.Messaging.message_initial_height
        # self.rect.height = constants.Messaging.message_height
        # self.rect.width += 10
    
    def run(self):
        if self.user:
            color = constants.Colors.BLUE
        else:
            color = constants.Colors.BLACK

        # self.rect.top = self.height
        # self.blit_text(self.screen, self.text, (self.left, self.height))
        # self.screen.blit(self.text, self.rect.move(5,5))
        # pygame.draw.rect(self.screen, color, self.rect, 2)
        self.render_multiline_text_with_border(self.text,200,self.font, (300,200))

    def setHeight(self, height):
        self.height = height

    def render_multiline_text_with_border(self, text, max_width, font, bottom_left):
        if self.user:
            border_color = constants.Colors.BLUE
        else:
            border_color = constants.Colors.BLACK
        lines = []
        words = text.split()
        current_line = ''
        for word in words:
            test_line = current_line + ' ' + word if current_line != '' else word
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word
        lines.append(current_line)
        
        # Render text
        text_surfaces = []
        for line in lines:
            text_surface = font.render(line, True, constants.Colors.BLACK)
            text_surfaces.append(text_surface)

        # Calculate bounding rectangle
        max_text_width = max(surface.get_width() for surface in text_surfaces)
        total_text_height = sum(surface.get_height() for surface in text_surfaces)
        self.total_text_height = total_text_height

        # Draw border around the text block
        border_rect = pygame.Rect(self.left, self.height - total_text_height - 5, max_text_width + 10, total_text_height + 10)
        if self.user:
            border_rect.right = (constants.game.screen_width - 17) 
        pygame.draw.rect(self.screen, border_color, border_rect, 2)

        # Blit text onto the screen
        y_offset = self.height - total_text_height
        for surface in text_surfaces:
            if self.user:
                self.screen.blit(surface, (constants.game.screen_width - border_rect.width - 12, y_offset))
            else:
                self.screen.blit(surface, (self.left + 5, y_offset))
            y_offset += surface.get_height()

    def get_total_text_height(self):
        return self.total_text_height
