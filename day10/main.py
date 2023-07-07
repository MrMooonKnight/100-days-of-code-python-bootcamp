from art import logo
from replit import clear

print(logo)

# Add
def add(n1, n2):
  return n1+n2
# Subtract
def subtract(n1,n2):
  return n1-n2
# Multiply
def multiply(n1,n2):
  return n1 * n2
# Divide
def divide(n1,n2):
  return n1/n2


# Creating a dictionary for operations
operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

calculator = True

num1 = int(input("Enter The First Number : "))
num2 = int(input("Enter The Second Number : "))

for operator in operations:
  print(operator)

operation_symbol = input("Select an Operation to Perform : ")
function = operations[operation_symbol]
result = function(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {result}")

while(calculator):
  choice = input("Type 'y' to continue calculating with {result} or type 'e' to Exit : ").lower()  
  if choice == "e":
    calculator = False
    break
  if choice == "y":
    num3 = int(input("Enter The Second Number : "))
    operation_symbol = input("Select an Operation to Perform : ")
    function = operations[operation_symbol]  
    result1 = function(result,num3)
    print(f"{result} {operation_symbol} {num3} = {result1}")
    result = result1
