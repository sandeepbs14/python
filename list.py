## LISTING ##

names = ["sandeep", "arnac", "anushka sen", "sachin"]
print(names[0])
names[1] = 'arnav'  # replacing the value in list

print(names)
print(len(names))  # to print length of list#
print(names[-2])  # to print 2nd from last#
print(names[-2:])  # to print from second-last to n[th] value

# to add another list to current list
names = names + ["virat kohli", "bhumrah"]
print(names)

# to add a value to the last of list
names.append("saurav")
print(names)

# to apped a value which is entered by user
names.append(input("enter a name to list"))  # enter a name which will print in console
print(names)
