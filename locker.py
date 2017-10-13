import pyperclip

class Credential:
    '''
    Class that will generate new instances
    '''
    password_list = []
    
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        
    def save_password(self):
        '''
        save credential objects to the password list
        '''
        Credential.password_list.append(self)

    def delete_password(self):
        '''
        remove credential objects from password list
        '''
        Credential.password_list.remove(self)