import pyperclip

class User:
    '''
    class that will create accounts for users
    '''
    user_list = []

    def __init__(self, login_name, password):
        self.login_name = login_name
        self.password = password

    def save_user(self):
        '''
        save user object to user list
        '''
        User.user_list.append(self)
    
    @classmethod
    def user_exist(cls, name, password):
        '''
        authenticate user if they have an account
        '''
        for user in User.user_list:
            if user.login_name == name and user.password == password:
                return user
            return False

    @classmethod
    def generate_password():
    '''
    function to generate a new password
    '''
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(10))

    return password