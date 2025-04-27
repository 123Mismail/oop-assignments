# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f"Dog name is : '{self.name}' and breed is : '{self.breed}' is barking.")
        
obj1:Dog = Dog("Raju" ,"German")
obj1.bark()

