import images
import constants
from text_input_field import Text_Input_Field
import pygame
from message import Message

class Character_Messenging:
    def __init__(self, screen, character, character_manager):
        self.screen = screen
        self.character = character
        self.character_manager = character_manager
        self.select_character_to_talk_to = images.Messaging.select_character
        self.rect = self.select_character_to_talk_to.get_rect()
        self.rect.topleft = (constants.Messaging_Select.width+2, 0)

        if character:
            self.character_image = images.Characters.character_dict_small[self.character]
            self.character_image_rect = self.character_image.get_rect()
            self.character_image_rect.center = constants.Messaging.character_image_pos

        self.send_message = images.Messaging.send_message
        self.send_message_rect = self.send_message.get_rect()
        self.send_message_rect.center = constants.Messaging.send_button_pos

        self.input_rect = pygame.Rect(162, 450, 538, 50)
        self.input = Text_Input_Field(self.screen, 30, self.input_rect)

        self.match_button = images.Messaging.match_button
        self.match_button_rect = self.match_button.get_rect()
        self.match_button_rect.center = constants.Messaging.match_button_pos

        self.top_panel_rect = pygame.Rect(152,0,constants.game.screen_width-152, 100)
        self.bottom_panel_rect = pygame.Rect(152,constants.game.screen_height-75,constants.game.screen_width-152,75)

        self.name_font = pygame.font.SysFont(None, 50)
        self.name = self.name_font.render(character,True, constants.Colors.BLACK)
        self.name_rect = self.name.get_rect()
        self.name_rect.center = constants.Messaging.character_name_pos

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
                    elif self.match_button_rect.collidepoint(event.pos):
                        self.match_button = images.Messaging.match_button_scaled
                        self.match_button_rect = images.Messaging.match_button_scaled.get_rect()
                    else:
                        self.send_message = images.Messaging.send_message
                        self.send_message_rect = images.Messaging.send_message.get_rect()
                        self.match_button = images.Messaging.match_button
                        self.match_button_rect = images.Messaging.match_button.get_rect()
                    self.send_message_rect.center = constants.Messaging.send_button_pos
                    self.match_button_rect.center = constants.Messaging.match_button_pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        if self.send_message_rect.collidepoint(event.pos):
                            sent_message = self.input.get_input()
                            self.messages.append(Message(self.screen, sent_message, True))
                            self.input.reset()
                            # self.messages.append(Message(self.screen, "Hi Liam, I'm Amy. It's a pleasure to meet you. I must admit, I'm a bit nervous. I hope we have a lot in common! What kind of things are you interested in?", False))
                            ai_message = self.character_manager.send_message(self.character, sent_message)
                            self.messages.append(Message(self.screen, ai_message, False))
            self.screen.fill(constants.Colors.LIGHT_GRAY, self.rect)
        
            total_height = 0
            for i in range(len(self.messages)):
                if i == 0:
                    self.messages[len(self.messages)-1-i].setHeight(constants.Messaging.message_initial_height + scroll_y)
                else:
                    total_height += self.messages[len(self.messages)-i].get_total_text_height() + 10
                    self.messages[len(self.messages)-1-i].setHeight(constants.Messaging.message_initial_height - total_height + scroll_y)
                    
                self.messages[len(self.messages)-1-i].run()
            
            pygame.draw.rect(self.screen, constants.Colors.GRAY, self.top_panel_rect)
            pygame.draw.rect(self.screen, constants.Colors.GRAY, self.bottom_panel_rect)
            self.screen.blit(self.match_button, self.match_button_rect)
            self.screen.blit(self.send_message, self.send_message_rect)
            self.screen.blit(self.character_image, self.character_image_rect)
            self.screen.blit(self.name, self.name_rect)
            
            self.input.run(events)


        

            

