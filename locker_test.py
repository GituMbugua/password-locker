import unittest
import pyperclip
from locker import Credential

class TestLocker(unittest.TestCase):
    def setUp(self):
        '''
        set-up method
        '''
        self.new_cred = Credential("gitu", "1234asdf") # password object
                

if __name__ == '__main__':
    unittest.main()