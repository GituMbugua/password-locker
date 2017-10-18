import unittest
from user import User

class TestLocker(unittest.TestCase):
    def setUp(self):
        '''
        set up method
        '''
        self.new_user = User("Gitu", "asdf1234") # new password object

    def test_init(self):
        '''
        test to see if the object is initializing
        '''
        self.assertEqual(self.new_user.login_name, "Gitu")
        self.assertEqual(self.new_user.password, "asdf1234")
    
    def tearDown(self):
        '''
        clean up after each test case runs
        '''
        User.user_list = []

    def test_save_user(self):
        '''
        test to see if the object is saved in the user list
        '''
        self.new_user.save_user() # save user
        self.assertEqual(len(User.user_list), 1)

if __name__ == '__main__':
    unittest.main()