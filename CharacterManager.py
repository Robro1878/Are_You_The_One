class CharacterManager:
    def __init__(self, characters: dict):
        self.characters = characters
        self.other_characters = self.characters.copy()

        self.gender_preference = None
        self.interest_preference = ''
        self.job_preference = ''
        self.values_preference = ''
    
    def setMainCharacter(self, character: str):
        self.MainCharacter = character
        self.other_characters.pop(self.MainCharacter)

    def getMainCharacter(self):
        return self.MainCharacter
    
    def setGender_Preference(self, preference):
        if preference == 'Male':
            self.gender_preference = 'Male'
            for character, traits in self.other_characters.copy().items():
                if traits['Gender'] == 'Female':
                    self.other_characters.pop(character)
        elif preference == 'Female':
            self.gender_preference = 'Female'
            for character, traits in self.other_characters.copy().items():
                if traits['Gender'] == 'Male':
                    self.other_characters.pop(character)
        else:    
            raise ValueError(f'Cannot choose {preference} as a preference')
        
        print(self.other_characters)
        
    def getGender_Preference(self):
        return self.gender_preference
    
    def setInterest_Preference(self, preference):
        self.interest_preference = preference

    def getInterest_Preference(self):
        return self.interest_preference
    
    def setJob_Preference(self, preference):
        self.job_preference = preference

    def getJob_Preference(self):
        return self.job_preference
    
    def setValues_Preference(self, preference):
        self.values_preference = preference
    
    def getValues_Preference(self):
        return self.values_preference