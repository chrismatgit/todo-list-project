passwords = {}

def store(pdict, username, password):
    pdict[username] = password

def create():
    for i in range(5):
        user = raw_input("Username: ")
        pas = raw_input("Password: ")
        store(passwords, user, pas)

create()

print passwords