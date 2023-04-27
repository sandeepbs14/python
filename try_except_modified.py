def division():
    i = int(input('enter first number: '))
    j = int(input('enter second number: '))
    try:
        divide = i / j
        print(divide)
    except ZeroDivisionError:
        print('cannot divide by zero')

print()
division()
print()
print('division completed')
