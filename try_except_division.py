i = int(input('enter a number'))
j = int(input('enter a number'))
try:
    divide = j / i
    print(divide)
    print('try completed')
except ZeroDivisionError:
    print('cannot divide by zero')
print('division completed')
