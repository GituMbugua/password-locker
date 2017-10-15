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
def display_passwords():
    '''
    function that returns all the saved passwords
    '''
    return Credential.display_passwords()


def main():
    print("Hello, welcome to Password Locker. What is your name?")
    first_name = input()
    
    while True:
            print(f"{first_name}, use the following codes: ac - add new credentials, sc - show all stored credentials, fc - find specific credentials, ex - exit ")
            
            short_code = input().lower()
            
            if short_code == 'ac':
                    print("New Credentials")
                    print("-" *10)
                    
                    print("Username....")
                    u_name = input()
                    
                    print("Password")
                    p_word = input()
                    
                    save_credentials(create_credential(u_name, p_word)) #create and save new cred
                    print('\n')
                    print(f"New Credential {u_name} {p_word} created")
                    print('\n')
                
            elif short_code == 'sc':
                    if display_passwords():
                            print("Here is a list of all your contacts")
                            print('\n')
                            
                            for contact in display_passwords():
                                    print(f"{credential.user_name} {credential.}")
                            print('\n')
                    else:
                            print('\n')
                            print("You do not have any credentials saved yet")
                            print('\n')
                            
            elif short_code == 'fc':
                    print("Enter the user name you want to search for")
                    
                    search_name = input()
                    if check_existing_credentials(search_name):
                            search_credential = find_credential(search_name)
                            print(f"{search_credential.user_name} {search_credential.password}")
                    else:
                        print("That credential cannot be found")
                        
            elif short_code == 'ex':
                    print("Goodbye...")
                    break
            else:
                print("Please use one of the short codes")
                
if __name__ == '__main__':
    main()