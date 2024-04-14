import pygame

#images
#Start Screen
class StartScreen:
    start_screen = pygame.image.load("images/start_screen.jpg")
    start_button = pygame.image.load("images/start_button.png")
    start_button_scaled = pygame.image.load("images/start_button_scaled.png")

#SelectCharacter
class SelectCharacter:
    background = pygame.image.load("images/select_character.png")
    left_arrow = pygame.image.load("images/left_arrow.png")
    right_arrow = pygame.image.load("images/right_arrow.png")
    left_arrow_scaled = pygame.image.load("images/left_arrow_scaled.png")
    right_arrow_scaled = pygame.image.load("images/right_arrow_scaled.png")
    select = pygame.image.load("images/Select_button.png")
    select_scaled = pygame.image.load("images/Select_button_scaled.png")

class SelectPreferences:
    background = pygame.image.load("images/select_preferences.png")
    male_symbol = pygame.image.load("images/male_symbol.png")
    male_symbol_scaled = pygame.image.load("images/male_symbol_scaled.png")
    female_symbol = pygame.image.load("images/female_symbol.png")
    female_symbol_scaled = pygame.image.load("images/female_symbol_scaled.png")
    next_button = pygame.image.load("images/next_button.png")
    next_button_scaled = pygame.image.load("images/next_button_scaled.png")
    

class Characters:
    Liam = pygame.image.load("images/characters/Liam.jpg")
    Ben = pygame.image.load("images/characters/Ben.jpg")
    Ethan = pygame.image.load("images/characters/Ethan.jpg")
    James = pygame.image.load("images/characters/James.jpg")
    Mason = pygame.image.load("images/characters/Mason.jpg")
    Noah = pygame.image.load("images/characters/Noah.jpg")
    Oliver = pygame.image.load("images/characters/Oliver.jpg")
    Will = pygame.image.load("images/characters/Will.jpg")
    Amy = pygame.image.load("images/characters/Amy.jpg")
    Ava = pygame.image.load("images/characters/Ava.jpg")
    Emma = pygame.image.load("images/characters/Emma.jpg")
    Izzy = pygame.image.load("images/characters/Izzy.jpg")
    Mia = pygame.image.load("images/characters/Mia.jpg")
    Olivia = pygame.image.load("images/characters/Olivia.jpg")
    Sophia = pygame.image.load("images/characters/Sophia.jpg")
    Zoe = pygame.image.load("images/characters/Zoe.jpg")

    Liam_small = pygame.image.load("images/characters/small/Liam.jpg")
    Ben_small = pygame.image.load("images/characters/small/Ben.jpg")
    Ethan_small = pygame.image.load("images/characters/small/Ethan.jpg")
    James_small = pygame.image.load("images/characters/small/James.jpg")
    Mason_small = pygame.image.load("images/characters/small/Mason.jpg")
    Noah_small = pygame.image.load("images/characters/small/Noah.jpg")
    Oliver_small = pygame.image.load("images/characters/small/Oliver.jpg")
    Will_small = pygame.image.load("images/characters/small/Will.jpg")
    Amy_small = pygame.image.load("images/characters/small/Amy.jpg")
    Ava_small = pygame.image.load("images/characters/small/Ava.jpg")
    Emma_small = pygame.image.load("images/characters/small/Emma.jpg")
    Izzy_small = pygame.image.load("images/characters/small/Izzy.jpg")
    Mia_small = pygame.image.load("images/characters/small/Mia.jpg")
    Olivia_small = pygame.image.load("images/characters/small/Olivia.jpg")
    Sophia_small = pygame.image.load("images/characters/small/Sophia.jpg")
    Zoe_small = pygame.image.load("images/characters/small/Zoe.jpg")



    character_list = [
        ['Liam',Liam],
        ['Ben',Ben],
        ['Ethan',Ethan],
        ['James',James],
        ['Mason',Mason],
        ['Noah',Noah],
        ['Oliver',Oliver],
        ['Will',Will],
        ['Amy', Amy],
        ['Ava', Ava],
        ['Emma', Emma],
        ['Izzy', Izzy],
        ['Mia', Mia],
        ['Olivia', Olivia],
        ['Sophia', Sophia],
        ['Zoe', Zoe],]
    
    character_dict = {
        'Liam':Liam,
        'Ben':Ben,
        'Ethan':Ethan,
        'James':James,
        'Mason':Mason,
        'Noah':Noah,
        'Oliver':Oliver,
        'Will':Will,
        'Amy':Amy,
        'Ava':Ava,
        'Emma':Emma,
        'Izzy':Izzy,
        'Mia':Mia,
        'Olivia':Olivia,
        'Sophia':Sophia,
        'Zoe':Zoe,}

    character_dict_small = {
        'Liam':Liam_small,
        'Ben':Ben_small,
        'Ethan':Ethan_small,
        'James':James_small,
        'Mason':Mason_small,
        'Noah':Noah_small,
        'Oliver':Oliver_small,
        'Will':Will_small,
        'Amy':Amy_small,
        'Ava':Ava_small,
        'Emma':Emma_small,
        'Izzy':Izzy_small,
        'Mia':Mia_small,
        'Olivia':Olivia_small,
        'Sophia':Sophia_small,
        'Zoe':Zoe_small}

class Messaging:
    select_character = pygame.image.load("images/select_character_to_talk_to.png")
    send_message = pygame.image.load("images/send_message.png")
    send_message_scaled = pygame.image.load("images/send_message_scaled.png")
    match_button = pygame.image.load("images/match.png")
    match_button_scaled = pygame.image.load("images/match_scaled.png")

class WinScreen:
    background = pygame.image.load("images/win_screen.jpg")

class LoseScreen:
    background = pygame.image.load("images/lose_screen.jpg")
    back_button = pygame.image.load("images/back_button.png")
    back_button_scaled = pygame.image.load("images/back_button_scaled.png")
