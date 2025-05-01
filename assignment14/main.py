 
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department
# object store a reference to an Employee object that exists independently of it.

class Employee:
  def __init__(self) -> None:
    print("Employee class is running ...")
  
  def employ_info(self):
    print("Employe is here .")

class Department:
  def __init__(self , employee) -> None:
     self.employee = employee
  def show_employ(self):
    return self.employee.employ_info()

employ :Employee = Employee()

depart :Department = Department(employ)
depart.show_employ()