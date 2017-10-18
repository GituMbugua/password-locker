import unittest
import pyperclip
from credential import Credential

class TestLocker(unittest.TestCase):
    def setUp(self):
        '''
        set-up method
        '''
        self.new_cred = Credential("Facebook", "gitu", "1234asdf") # password object

    def test_init(self):
        '''
        test to see if the object is initializing
        '''
        self.assertEqual(self.new_cred.website, "Facebook")
        self.assertEqual(self.new_cred.user_name, "gitu")
        self.assertEqual(self.new_cred.password, "1234asdf")

    def tearDown(self):
        '''
        clean up after each test case runs
        '''
        Credential.credential_list = []

    def test_save_credential(self):
        '''
        test to see if the object is saved in the credential list
        '''
        self.new_cred.save_credential() # save the credential
        self.assertEqual(len(Credential.credential_list), 1)

    def test_delete_credential(self):
        '''
        test to see if a credential can be deleted
        '''
        self.new_cred.save_credential()
        test_credential = Credential("Facebook", "gitu", "1234asdf") # new credentials
        test_credential.save_credential()
        
        self.new_cred.delete_credential() # delete credential object
        self.assertEqual(len(Credential.credential_list), 1)

    def test_find_password_by_username(self):
        '''
        test to see if we can find a password using the username
        '''
        self.new_cred.save_credential()
        test_credential = Credential("Facebook", "gitu", "1234asdf")
        test_credential.save_credential()
        found_credential = Credential.find_by_username("gitu")
        
        self.assertEqual(found_credential.password, test_credential.password)
        
    def test_credential_exists(self):
        '''
        test to see if we can return a boolean if a credential is not found
        '''
        self.new_cred.save_credential()
        test_credential = Credential("Facebook", "gitu", "1234asdf")
        test_credential.save_credential()
        
        credential_exists = Credential.credential_exist("gitu")
        
        self.assertTrue(credential_exists)
        
        

    def test_display_all_credentials(self):
        '''
        returns a list of all saved credentials
        '''
        self.assertEqual(Credential.display_credentials(), Credential.credential_list)
        
    def test_copy_username(self):
        '''
        test to confirm that a username can be copied from a found credential
        '''
        self.new_cred.save_credential()
        Credential.copy_user_name("gitu")
        
        self.assertEqual(self.new_cred.user_name, pyperclip.paste())

if __name__ == '__main__':
    unittest.main()