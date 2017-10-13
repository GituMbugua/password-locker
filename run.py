#!/usr/bin/env python3.6
from locker import Credential

def create_credential(uname, password):
    '''
    function to create a new contact
    '''
    new_cred = Credential(uname, password)
    return new_cred