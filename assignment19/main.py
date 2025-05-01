 
def add_greeting(cls):
    def greet(self):
        return f"Hello from Decorator, {self.name}!"
    cls.greet = greet
    return cls
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name
if __name__ == "__main__":
    p = Person("Ismail")
    print(p.name)        
    print(p.greet())      
