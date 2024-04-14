from characterai import pycai
from constants import AIPrompts

class Chatbot:
    def __init__(self, name, interests, job, values):

        self.client = pycai.Client('39cf52482c896ef0c48e7be264537d9ff828c10d')
        self.name = name
        self.interests = interests
        self.job = job
        self.values = values
        self.character = None
        self.chat = None

    def format_attributes(self, attributes):    
        num_attributes = len(attributes)
        
        if num_attributes == 1:
            return attributes[0]
        elif num_attributes == 2:
            return " and ".join(attributes)
        else:
            formatted_attributes = ", ".join(attributes[:-1])
            return f"{formatted_attributes}, and {attributes[-1]}"
    
    def create_character(self):
        self.character = self.client.create_char(
            name=self.name, greeting=f"Hi I'm {self.name}", 
            description=AIPrompts.description.format(job = self.job, 
                                        interests = self.format_attributes(self.interests), 
                                        values = self.format_attributes(self.values)))
        
        self.char_id = self.character.external_id
        info = self.client.get_me()
        self.creator_id = info.id
        print(f'created character {self.name}')
    
    def send_message(self, text):
        print(f'Attempting to send message to {self.name}')
        with self.client.connect() as chat:
            if self.chat is None:
                print(f'Attempting to create chat for {self.name}')
                self.chat, answer = chat.new_chat(self.char_id, self.creator_id,)
                print(f"Created chat for {self.name}")
    
            message = chat.send_message(self.char_id, self.chat.chat_id, text)
            print(f'Sent {text} to {self.name}')

        
        return message.text








