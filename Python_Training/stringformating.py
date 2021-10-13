# age = 30
# print("My age is " + str(age) + " years")
# print("My age is {0} years".format(age))    # coerce.. replacing the {} values with the age variable
#
# print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7} ".format("31", "January", "March", "May", "July", "August", "October", "December")
#       +"months")
#
# print("""
# Jan : {1}
# Feb : {0}
# Mar : {1}
# Apr : {2}""".format(28,31,30))
#
# print()
# # String Formatting
# for i in range(1, 15):
#     # print("Number {0} have square value as {1} and cube value as {2}".format(i, i ** 2 , i ** 3))
#     print("Number {0:2} have square value as {1:3} and cube value as {2:4}".format(i, i ** 2 , i ** 3)) #creating space/memory for the extra chars
#
# print()
# for i in range(1, 15):
#     print("Number {0:2} have square value as {1:<3} and cube value as {2:<4}".format(i, i ** 2 , i ** 3)) #creating space/memory for the extra chars
#
# print()
# for i in range(1, 15):
#     print("Number {0:2} have square value as {1:^3} and cube value as {2:^4}".format(i, i ** 2 , i ** 3)) #creating space/memory for the extra chars

print()
print("Pi is of value {0:12}".format(22/7))     # 0 is the assigned value in format function and 15 is the default decimal character limit.
print("Pi is of value {0:12f}".format(22/7))    # f is the floating point character for 6 decimal digits
print("Pi is of value {0:12.50f}".format(22/7)) # 50 decimal characters using float
print("Pi is of value {0:52.50f}".format(22/7))
print("Pi is of value {0:62.50f}".format(22/7))
print("Pi is of value {0:^72.50f}".format(22/7))


