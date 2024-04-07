import pygame

class game:
    screen_width = 768
    screen_height = 512
    window_title = "Are you the one?"
    fps = 60
    characters = {"Amy": {'Gender' : 'Female'},
                  "Ava": {'Gender' : 'Female'},
                  "Ben": {'Gender' : 'Male'},
                  "Emma": {'Gender' : 'Female'},
                  "Ethan": {'Gender' : 'Male'},
                  "Izzy": {'Gender' : 'Female'},
                  "James": {'Gender' : 'Male'},
                  "Liam": {'Gender' : 'Male'},
                  "Mason": {'Gender' : 'Male'},
                  "Mia": {'Gender' : 'Female'},
                  "Noah": {'Gender' : 'Male'},
                  "Oliver": {'Gender' : 'Male'},
                  "Olivia": {'Gender' : 'Female'},
                  "Sophia": {'Gender' : 'Female'},
                  "Will": {'Gender' : 'Male'},
                  "Zoe": {'Gender' : 'Female'}}

class StartScreen:
    start_button_pos = (685,383)

#Select Character
class SelectCharacter:
    left_arrow_pos = (game.screen_width//6, game.screen_height//2 + 30)
    right_arrow_pos = ((game.screen_width//6)*5, game.screen_height//2 + 30)
    character_pos = (game.screen_width//2, game.screen_height//2 + 30)
    select_pos = (660,430)

class SelectPreferences:
    interests_input_rect = pygame.Rect(480,180, 250,50)
    job_input_rect = pygame.Rect(50,350, 250,50)
    values_input_rect = pygame.Rect(480,350, 250, 50)

    male_symbol_pos = (250,225)
    female_symbol_pos = (100, 225)

    next_button_pos = (game.screen_width//2, 450)

class Messaging_Select:
    width = 150
    fontsize = 30

class Colors:
    GREEN = (0, 255, 0)
    BLUE = (0,0,255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    LIGHT_GRAY = (219, 219, 219)