
# Assignment:
# Create a class Student with attributes name and marks. Use the   self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
  def __init__(self ,name , marks) -> None:
     self.name:str = name
     self.marks:int =marks
  def display(self ):
     return f"Student name : {self.name} and marks gained : {self.marks}"
student1:Student = Student("Muhammad Ismail" ,"23")
student1.display() 