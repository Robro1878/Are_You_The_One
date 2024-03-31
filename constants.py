class game:
    screen_width = 768
    screen_height = 512
    window_title = "Are you the one?"
    fps = 60
    characters = {"Amy","Ava","Ben","Emma","Ethan", "Izzy", "James", "Liam", "Mason", "Mia", "Noah", "Oliver", "Olivia", "Sophia", "Will", "Zoe"}

class StartScreen:
    start_button_pos = (685,383)

#Select Character
class SelectCharacter:
    left_arrow_pos = (game.screen_width//6, game.screen_height//2 + 30)
    right_arrow_pos = ((game.screen_width//6)*5, game.screen_height//2 + 30)
    character_pos = (game.screen_width//2, game.screen_height//2 + 30)
    select_pos = (660,430)