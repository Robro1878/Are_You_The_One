from participant import Participant

class Other_Contestant(Participant):
    def __init__(self, name, gender, match):
        '''Creates a new other_contestant'''
        super().__init__(name, gender, match)
    
    def talk(context):
        '''Returns a string containing dialogue relating to the context'''
        #Not sure what this will be like yet
        pass

