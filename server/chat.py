"""
Represents and store information about the chat
"""
class Chat:
    
    def __init__(self):
        self.__chat = []
        
    @property
    def chat(self):
        return self.__chat
    
    @chat.setter
    def chat(self, msg):
        self.__chat.append(msg)
        
    def __len__(self):
        return len(self.__chat)
    
    def __str__(self):
        return "".join(self.__chat)
    
    def __repr__(self):
        return str(self)