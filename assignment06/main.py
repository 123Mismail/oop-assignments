# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("object instance is construted.")
        
    def __del__(self):
        print("Object instance is deleted.")

# object instance is creating here 
obj1:Logger =Logger()
print(obj1)
del obj1