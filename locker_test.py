import unittest
import pyperclip
from locker import Credential

class TestLocker(unittest.TestCase):
    def setUp(self):
        '''
        set-up method
        '''
        self.new_cred = Credential("gitu", "1234asdf") # password object

    def test_init(self):
        '''
        test to see if the object is initializing
        '''
        self.assertEqual(self.new_cred.user_name, "gitu")
        self.assertEqual(self.new_cred.password, "1234asdf")

    def test_save_password(self):
        '''
        test to see if the object is saved in the password list
        '''
        self.new_cred.save_password() # save the password
        self.assertEqual(len(Credential.password_list), 1)

    def test_delete_password(self):
        '''
        test to see if a credential can be deleted
        '''
        self.new_cred.save_password()
        test_password = Credential("gitu", "1234asdf") # new credentials
        test_password.save_password()
        
        self.new_cred.delete_password() # delete contact object
        self.assertEqual(len(Credential.password_list), 1)
                

if __name__ == '__main__':
    unittest.main()