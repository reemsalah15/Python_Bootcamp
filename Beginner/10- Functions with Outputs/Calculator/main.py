from art import logo
from replit import clear

def add(first_num, next_num):
  return first_num + next_num
  
def subtract(first_num, next_num):
  return first_num - next_num
  
def multiply(first_num, next_num):
  return first_num * next_num
  
def divide(first_num, next_num):
  return first_num / next_num
    
def calculator_prog():
  print(logo)
  first_num = float(input("What's the first number?: "))
  for operator in dic_of_operation:
      print(operator)
  
  while True:       
    my_operation = input("Pick up an operation: ")
    next_num = float(input("What's the next number?: "))
    calculator = dic_of_operation[my_operation]
    result = calculator(first_num,next_num)
    
 
    
    print(f"{first_num} {my_operation} {next_num} = {result}")
    
    should_continue = input(f"Type \'y' to continue calculating with {result} or type \'n' to start a new calculation: ")
    if should_continue == "y":
      first_num = result
    else:
      clear()
      calculator_prog()

calculator_prog()  
  