import pyperclip

class Credential:
    '''
    Class that will generate new instances
    '''
    credential_list = []
    
    def __init__(self, website, user_name, password):
        self.website = website
        self.user_name = user_name
        self.password = password
        
    def save_credential(self):
        '''
        save credential objects to the credential list
        '''
        Credential.credential_list.append(self)

    def delete_credential(self):
        '''
        remove credential objects from credential list
        '''
        Credential.credential_list.remove(self)

    @classmethod    
    def find_by_username(cls, name):
        '''
        method takes in the user name and returns a credential that matches it
        '''
        for credential in cls.credential_list:
            if credential.user_name == name:
                return credential
            
    @classmethod
    def credential_exist(cls, name):
        for credential in cls.credential_list:
            if credential.user_name == name:
                return True
        return False
    
    @classmethod
    def display_credentials(cls):
        '''
        returns the credential list
        '''
        return cls.credential_list

    @classmethod
    def copy_user_name(cls, name):
        credential_found = Credential.find_by_username(name)
        pyperclip.copy(credential_found.user_name)