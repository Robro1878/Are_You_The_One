import random
import CharacterTraits

class CharacterManager:
    def __init__(self, characters: dict):
        self.characters = characters
        self.other_characters = self.characters.copy()

        self.gender_preference = None
        self.interest_preference = ''
        self.job_preference = ''
        self.values_preference = ''

        self.match = ''
    
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
    
    def randomizeOtherPlayerTraits(self):
        '''Randomly selects a character to be the match and randomly assigns traits to other characters'''

        #Sets one other player to be a 'perfect match'
        self.match = random.choice(list(self.other_characters.keys()))
        self.other_characters[self.match]['Interests'] = self.interest_preference
        self.other_characters[self.match]['Job'] = self.job_preference
        self.other_characters[self.match]['Values'] = self.values_preference
        
        #all other players are set to have random traits
        for character, traits in self.other_characters.items():
            if character != self.match:
                traits['Interests'] = [random.choice(CharacterTraits.interests) for i in range(random.randint(1,3))]
                traits['Job'] = random.choice(CharacterTraits.jobs) 
                traits['Values'] = [random.choice(CharacterTraits.values) for i in range(random.randint(1,3))]

        print(self.other_characters)
    
    def getOtherCharacters(self):
        return self.other_characters

        
        
