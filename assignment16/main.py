# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:
# A with a method show(),
# B and C that inherit from A and override show(),
# D that inherits from both B and C.
# Create an object of D and call show() to observe MRO.

class A:
  def show(self):
    print("Show method of class A .")
  
class B(A):
  def show(self):
    print("Show method of class B .")

class C(A):
  def show(self):
    print("Show method of class C .")

class D( B , C ):
  pass

d = D()
print(D.__mro__)
d.show()
