class CharacterManager:
    def __init__(self, characters: dict):
        self.characters = characters
    
    def setMainCharacter(self, character: str):
        self.MainCharacter = character

    def getMainCharacter(self):
        return self.MainCharacter