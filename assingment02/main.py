
#  Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Car:
  count = 0
  def __init__(self) -> None:
    #  self.count += 1 # self.count means i am initializing a new varable name count but it will not increase the count value .
    
     Car.count +=1 # this line of code will increase the count value every time when a new instance of this class madd 
  @classmethod
  def track_instance (cls):
    return f"No of ojects made on the class is {cls.count}"
obj1:Car =Car()
obj2:Car =Car()
obj3:Car =Car()
obj4:Car =Car()
print(obj1.track_instance())  