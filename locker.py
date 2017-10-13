import pyperclip

class Credential:
    '''
    Class that will generate new instances
    '''
    password_list = []
    
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        
    