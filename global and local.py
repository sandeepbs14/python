
print("global and local variable")

number = 10
def num():
   # number = 11#
    i=number+1
    print(i)

num()
print(number)

print("---------------------================-------------------------")

def addition(a,b):
    sum=a+b
    return sum
i=int(input('enter a digit'))
j=int(input('enter a digit'))

total=addition(i,j)
print(total)













