def multiply():
    i = int(input("how long should be the result: "))
    x = int(input("enter number to multiply: "))
    z = int(input("enter no from which u need result: "))
    if x == 0:
        print('cannot divide by zero')

    else:
        for r in range(z, i, x):
            print(r)

result = multiply()
print(result)
