# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor.
#  Define a __call__() method that multiplies an input by the factor.
#  Test it with callable() and by calling the object like a function.

class Multiplier:
  def __init__(self,num) -> None:
     self.num = num
     
  def __call__(self,multp) ->None:
     fact = self.num * multp
     print(fact) 

obj : Multiplier = Multiplier(2)
print(callable(obj)) # output : True 
obj(12)

