class Dog:
    race = "dark"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True
        
    def eat(self):
        self.is_hungry = False


class Pets:
        
    mex = Dog("mex", 4)
    sol = Dog("sol", 8)
    kiki = Dog("kiki", 6)
    mex.eat()
    sol.eat()
    kiki.eat()

pets = Pets()

info = f"""
    I have 3 dogs.
    {pets.mex.name} is {pets.mex.age}
    {pets.sol.name} is {pets.sol.age}
    {pets.kiki.name} is {pets.kiki.age}
    kiki race is {pets.kiki.race}
    
"""
print(info)
status = pets.mex.is_hungry == False and pets.sol.is_hungry == False and pets.kiki.is_hungry == False

if status:
    print("My dogs are not hungry!")
