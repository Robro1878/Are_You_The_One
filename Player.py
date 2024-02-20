from participant import Participant

class Player(Participant):
    def __init__(self, name, gender, match):
        '''Creates a new player'''
        super().__init__(name, gender, match)

    def check_match(self, contestant):
        '''Returns true if player and contestant are a match'''
        return self.match == contestant and contestant.match == self

