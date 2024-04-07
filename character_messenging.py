import images
import constants
from text_input_field import Text_Input_Field
import pygame

class Character_Messenging:
    def __init__(self, screen, character):
        self.screen = screen
        self.character = character
        self.select_character_to_talk_to = images.Messaging.select_character
        self.rect = self.select_character_to_talk_to.get_rect()
        self.rect.topleft = (constants.Messaging_Select.width+2, 0)

        self.send_message = images.Messaging.send_message
        self.send_message_rect = self.send_message.get_rect()
        self.send_message_rect.topleft = (712,450)


        self.input_rect = pygame.Rect(162, 450, 538, 50)
        self.input = Text_Input_Field(self.screen, 30, self.input_rect)

    def run(self, events, scroll_y):
        if self.character is None:
            self.screen.blit(self.select_character_to_talk_to, self.rect)
        else:
            self.screen.fill(constants.Colors.LIGHT_GRAY, self.rect)
            self.input.run(events)
            self.screen.blit(self.send_message, self.send_message_rect)
        

            

