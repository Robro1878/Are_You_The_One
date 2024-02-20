class Participant:
    def __init__(self, name, gender, match):
        '''Creates a new participant'''
        self.name = name
        self.gender = gender
        self.match = match
        self.preferences = []

    def add_preference(self, preference):
        '''adds a preference'''
        self.preferences.append(preference)
    