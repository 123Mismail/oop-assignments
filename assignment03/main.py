class Car:
  brand:str = "Toyota"
  def __init__(self):
    pass
  def start(self):
    print("Car is satrting ....")
car1:Car= Car()
car1.brand
print(car1.brand)
car1.start()