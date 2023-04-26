def user(*values):
    print("my name is: " + values[0], ", my age is :" + str(values[1]), ", sex is : " + values[2],
          ", your bday is :" + str(values[3]))


i = input("enter your name :")
j = input("enter your age :")
k = input("choose sex :")
l = input("enter date of birth :")

user(i, j, k, l)


print('----------------------------------------------------------------------')
print()

print("global and local variable")
