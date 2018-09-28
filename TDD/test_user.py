import unittest
import re
from user import User

class TestUserAccount(unittest.TestCase):
    def setUp(self):
        self.user = User()
        self.email = "christianmatabaro@gmail.com"
        self.password = "123Dchris!*"
        self.username = "chrismat"
        self.name = "chris"
        self.age = 23


        self.user_account = dict(
            username = self.username,            
            email = self.email,
            age = self.age,
            password = self.password
        ) 

    def test_initiattion(self):
        self.assertIsInstance(self.user, User)

    def test_email_validation(self):
        self.assertTrue(self.user.email_validation(self.email))
        
    def test_password_validation(self):
        self.assertTrue(self.user.password_validation(self.password))
        self.assertFalse(self.user.password_validation("bhjhjh"))

    def test_username_validation(self):
        self.assertTrue(self.user.username_validation(self.username, self.name))

    def test_age_validation(self):
        self.assertTrue(self.user.age_validation(self.age)) 
        self.assertFalse(self.user.age_validation(0))

    def test_user_registration(self):
        self.assertEqual(len(self.user.users), 0)
        self.user.user_registration(self.name, **self.user_account)
        self.assertEqual(len(self.user.users), 1)

    def test_duplicate_users(self):
        self.user.user_registration(self.name, **self.user_account)
        self.assertFalse(self.user.user_registration(self.name, **self.user_account))
    
    def test_user_login(self):
        self.user.user_registration(self.name, **self.user_account)
        self.assertTrue(self.user.user_login(self.username, self.password))
        self.assertFalse(self.user.user_login("gg", "poeple"))


