# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property 
# to get the price, @price.setter to update it,
#  and @price.deleter to delete it.
class Product:
  def __init__(self,name,price) -> None:
     self.name = name 
     self.__price = price
  @property
  def price(self):
    print("accessing private variable price value.")
    return self.__price
  @price.setter
  def price(self, new_val):
    self.__price = new_val
    print(f"updated value of : {self.__price }")
  @price.deleter
  def price(self):
    print("Object is deleting here .")
    del self.__price
obj1:Product = Product("Gold",48555)
obj1.price
obj1.price=454545
del obj1.price


