# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called"
#  before a function executes. Apply it to a function say_hello().
def log_function_call(func):
  def inner():
    print("funciton is being called .")
    func()
    print("After funciton called.")

  return inner

@log_function_call
def say_hello():
  print("Hello World.")

say_hello()