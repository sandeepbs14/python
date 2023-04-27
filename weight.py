weight = int(input("enter the weight: "))
unit = input("weight in 'K'g or 'L'bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("weight in Lbs: " + str(converted))
elif unit.upper() == "L":
    converted = weight * 0.45
    print("weight in KGs: " + str(converted))
else:
    print("enter k or l")
    print('completed!!!')
