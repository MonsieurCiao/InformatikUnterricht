# calculator
a = float(input('first number: '))
b = float(input('second number: '))
operation = input('operation: ')

def switch(operation):
  if operation == '+':
    return a + b
  elif operation == '-':
    return a - b
  elif operation == '*':
    return a * b
  elif operation == '/':
    if b != 0:
      return a/b
    else:
      return "Can't divide by zero"
  else:
    return 'Did you type in a valid operation'

print('Your result = ', switch(operation))