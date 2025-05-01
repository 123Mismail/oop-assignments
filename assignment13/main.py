 
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.


class Engine:
  def start(self):
    print("Engine is startng .....")

class Car:
  def __init__(self):
     self.engine = Engine()
  def start_engie(self):
    return self.engine.start()
  
car = Car()
print(car.start_engie())