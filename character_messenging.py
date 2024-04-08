import images
import constants
from text_input_field import Text_Input_Field
import pygame
from message import Message

class Character_Messenging:
    def __init__(self, screen, character):
        self.screen = screen
        self.character = character
        self.select_character_to_talk_to = images.Messaging.select_character
        self.rect = self.select_character_to_talk_to.get_rect()
        self.rect.topleft = (constants.Messaging_Select.width+2, 0)

        self.send_message = images.Messaging.send_message
        self.send_message_rect = self.send_message.get_rect()
        self.send_message_rect.center = constants.Messaging.send_button_pos

        self.input_rect = pygame.Rect(162, 450, 538, 50)
        self.input = Text_Input_Field(self.screen, 30, self.input_rect)

        self.messages = []

    def run(self, events, scroll_y):
        if self.character is None:
            self.screen.blit(self.select_character_to_talk_to, self.rect)
        else:
            for event in events:
                if event.type == pygame.MOUSEMOTION:
                    #check if mouse is in button area
                    if self.send_message_rect.collidepoint(event.pos):
                        self.send_message = images.Messaging.send_message_scaled
                        self.send_message_rect = images.Messaging.send_message_scaled.get_rect()
                    else:
                        self.send_message = images.Messaging.send_message
                        self.send_message_rect = images.Messaging.send_message.get_rect()
                    self.send_message_rect.center = constants.Messaging.send_button_pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        if self.send_message_rect.collidepoint(event.pos):
                            self.messages.append(Message(self.screen, self.input.get_input(), True))
                            self.input.reset()
            self.screen.fill(constants.Colors.LIGHT_GRAY, self.rect)
            self.input.run(events)
            self.screen.blit(self.send_message, self.send_message_rect)
            for i in range(len(self.messages)):
                self.messages[len(self.messages)-1-i].setHeight(constants.Messaging.message_initial_height - i*constants.Messaging.message_height_delta + scroll_y)
                self.messages[len(self.messages)-1-i].run()



        

            

