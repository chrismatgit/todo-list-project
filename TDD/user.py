import re
class User:
    def __init__(self):
        self.users = []

    def email_validation(self, email):
        if email and not re.findall(r'[\w\.-]+@[\w\.-]+', email):
            raise ValueError("Enter a valid email address")
        else:
            return True

        if email =="" and email ==" ":
            raise ValueError("Email cant be empty")
        else:
            return True

    def password_validation(self, password):
        number = re.search(r"[0-9]", password)
        symbols = re.search('[@_!#$%^&*()<>?/\|}{~:]',password)
        lowercase = re.search(r"[a-z]", password)
        uppercase = re.search(r"[A-Z]", password)
        
        if  number and symbols and lowercase and uppercase and len(password) >= 4:
            return True
        else:
            return False
        
    def username_validation(self, username, name):
        if username and name and username != name and len(username) >= 4:
            return True
        else:
            return False

    def age_validation(self, age):
        if isinstance(age, int) and age > 0:
            return True
        else:
            return False

    def user_registration(self, name, **kwargs):
        username = kwargs["username"]
        email = kwargs["email"]
        age  = kwargs["age"]
        password = kwargs["password"]
    
        user = dict(
            name = name,
            username = self.username_validation(username, name),
            email = self.email_validation(email),
            age = self.age_validation(age),            
            password = self.password_validation(password)
        )

        if user not in self.users:
            self.users.append(user)
        else:
            print("User already exists")
            return False

    def user_login(self, username, password):
        """ Checks True if both password and username are a match"""
        for user in self.users:
            name = user['name']
            if username and self.username_validation(username, name) == user['username'] and \
                self.password_validation(password) == user['password']:
                print("You're logged in")
                return True
            else:
                return False



   
        
        