# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.
class Person:
  def __init__(self,name,category) -> None:
     self.name =name
     self.category=category

class Teacher(Person):
  def __init__(self, subject,name,category) -> None:
     super().__init__(name,category)

     self.name =name
     self.category =category
     self.subject =subject

person1:Person =Person("Shabbir khan","Homosepiense")
teacher1:Teacher =Teacher("Muhammad Ismail","AI Engineer","Homosepiense")
print(person1.name)
print(teacher1.name)
print(teacher1.subject)
print(teacher1.category)

