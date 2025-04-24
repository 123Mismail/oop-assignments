# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank :
  bank_name :str ="Bank Alfalah"
  print(bank_name)
  def __init__(self) -> None:
     pass 
  @classmethod
  def chande_bank_name(cls , name):
    cls.bank_name = name
obj1 :Bank =Bank()
obj1.chande_bank_name("UBL Bank")

print(obj1.bank_name)
  
