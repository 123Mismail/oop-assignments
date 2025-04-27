
# Access modifiers
class Employee:
  def __init__(self ,name ,salary ,PIN) -> None:
     self.name =name
     self._salary = salary
     self.__PIN = PIN

obj1:Employee =Employee("muhammad Ismail","2000k","Balti1234")

name = obj1.name
# protected is leacked because python doesnt stricktly follows the access modifiers rules 
salary_ =obj1._salary
# here you will get error as __PIN is private but still you get get access this also by name mangling , as python stores this internally like _Employee__PIN 
# pin__ = obj1.__PIN
# but this technique is not recomended as conventions says protected and privates are only can us inside the class and _protected can be use in subclass
pin__ = obj1._Employee__PIN


print(name)
print(salary_)
print(pin__)

# document 
#  Key Takeaways: Access Modifiers in Python Classes
# 1. Public Variables (name)
# Defined like self.name

# Accessible from anywhere

# Example: obj1.name

# 2. Protected Variables (_salary)
# Defined with a single underscore: self._salary

# Accessible from outside, but by convention should be treated as internal

# Example: obj1._salary

# Used when a variable is "protected" but not strictly private

# 3. Private Variables (__PIN)
# Defined with double underscores: self.__PIN

# Not directly accessible due to name mangling

# Internally renamed to _ClassName__var (e.g., _Employee__PIN)

# Can still be accessed via: obj1._Employee__PIN (not recommended)

