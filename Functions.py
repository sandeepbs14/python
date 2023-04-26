print("This is a sample file of functions")


def prt():
    print("hello world")


prt()

print('------------------------------------------------------------------------')


def name(names):
    print("my name is-:" + names)


name("sandeep")

print('------------------------------------------------------------------------')


def name(a):
    print("my name is: " + a)


i = input("enter your name: ")


def age(b):
    print("your age is: " + b)


j = input("enter your age: ")
name(i)
age(j)

print('---------------------------------------------------------------------------')


def user(name, age, sex, dob):
    print("my name is: " + name)
    print("age :" + str(age))
    print("sex :" + sex)
    print("date of birth :" + str(dob))


i = input("enter your name :")
j = input("enter your age :")
k = input("choose sex :")
l = input("enter date of birth :")

user(i, j, k, l)

print("-------------------------------------------------------------------------")
print('function simplifies')


def user(*values):
    print("my name is: " + values[0], ", my age is :" + str(values[1]), ", sex is : " + values[2],
          ", your bday is :" + str(values[3]))


i = input("enter your name :")
j = int(input("enter your age :"))
k = input("choose sex :")
l = int(input("enter date of birth :"))

user(i, j, k, l)
