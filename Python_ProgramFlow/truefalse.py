# day = "Friday"
# temperature = 27
# raining = False
#
# if day == "Saturday" and temperature > 26 and not raining:
#     print("GO out for chill!")
# else:
#     print("Stay at home!")

print()
if not 0:   # 0 is considered as False
    print("This is false interpretation")
else:
    print("This is true interpretation")

name = input("Please enter your name? ")
if name:
    print("Hello {}".format(name))
else:
    print("You dont have a name right?")