# Assignment:
# Create a class TemperatureConverter with a 
# static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.
class TemperatureConverter:
  def __init__(self) -> None:
     pass
  @staticmethod
  def celsius_to_fahrenheit(c):
    """
    Takes one argument as celsius in numbers and convert them into fahrenheight 
    """
    F= (c*(9/5))+32
    return f"{c} celsius is equals to {F:.3f} Fahrenheight."
obj1:TemperatureConverter = TemperatureConverter()
obj1.celsius_to_fahrenheit(45)



