class game:
    screen_width = 768
    screen_height = 512
    window_title = "Are you the one?"
    fps = 60
    characters = {"Amy": None,"Ava": None,"Ben": None,"Emma": None,"Ethan": None, "Izzy": None, "James": None, "Liam": None, "Mason": None, "Mia": None, "Noah": None, "Oliver": None, "Olivia": None, "Sophia": None, "Will": None, "Zoe": None}

class StartScreen:
    start_button_pos = (685,383)

#Select Character
class SelectCharacter:
    left_arrow_pos = (game.screen_width//6, game.screen_height//2 + 30)
    right_arrow_pos = ((game.screen_width//6)*5, game.screen_height//2 + 30)
    character_pos = (game.screen_width//2, game.screen_height//2 + 30)
    select_pos = (660,430)