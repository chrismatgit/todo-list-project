# This file contains code for managing your account

accounts = {
    "password" : "User"
}  # dictionary where key is the  password and value is User

def add_account(name, password):
    accounts[password] = name
    
"""
    Adds the key value pair to the accounts dictionary

"""
# users = passwords = ''
# def add_user_details():
#     for a in range(1):
#         users = raw_input("Please enter a Name to create an account: ")
#         passwords = raw_input("Type your Password to create an account: ")
#         add_account(users, passwords)
#add_user_details()

pass

"""

    returns true if the password and corresponding name exist in the 

    accounts dicitionary

"""


def login(name, password):
    if password in accounts:
        if name == accounts[password]:
            print('login successfull\n')
            return True
        else:
            return False
    else:
            return False
