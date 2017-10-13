#!/usr/bin/env python3.6
from locker import Credential

def create_credential(uname, password):
    '''
    function to create a new credential
    '''
    new_cred = Credential(uname, password)
    return new_cred

def save_credentials(cred):
    '''
    function to create a new credential
    '''
    cred.save_password()
    
def del_credential(cred):
    '''
    function to delete a credential
    '''
    cred.delete_password()
    
def find_credential(uname):
    '''
    function that finds a credential by the username and returns it
    '''
    return Credential.find_by_username(uname)