# # print('This is my first code')
# # print("Python's string is easy to use")
# # print('Say "Hello" to my friend!')
# #
# # print("Hello" + " World")
# # firstname = 'Piyush'
# # lastname = 'Sultania'
# # lastnameparam = input("Please enter your last name ")
# # print(firstname+' '+lastnameparam)
# #
# # #prompt for value
# # age1 = 24
# # age = input("Please enter the age: ")
# # print("My age is : " + age)
# #
# # print(type(firstname))
# # print(type(age1))
# #
# # age2= '2 years'
# # print(type(age2))
# #
# # # str will convert any data type to string
# # f_name = "Piyush"
# # f_age = 23
# # print(f_name + " is having an age of " + str(f_age))
# #
# # print()
#
# # print(parrot[3])
# # print(parrot[4])
# # print()
# # print(parrot[3])
# # print(parrot[6])
# # print(parrot[8])
# # print("")
# #
# # # negative indexing!
# # print(parrot[-11])
# # print(parrot[-1])
# # print()
# # print(parrot[-11])
# # print(parrot[-8])
# # print(parrot[-6])
#
# # # Slicing...
# # # Start, stop and step values
# # print(parrot[0:6])  # Norweg - Stop index is not counted, upto but not including
# # print(parrot[3:5])
# # print(parrot[2:])
# # print(parrot[:5])
# # print(parrot[10:])
# #
# # a = 3
# # b = 5
# # print(parrot[a:b])
# #
# # print(parrot[:20])
# # #print(parrot[16:])  # blank as index does not found for start character
# # print(parrot[2:33])
# # #print(parrot[22])
# # print("")
# # print(parrot[0:6] + parrot[6:])
# # print(parrot[:])    # if no start and end then it will take whole string
#
# # for i in range(1,10):
# #     print(i)
# #print(parrot)
#
# # print(parrot[-4:2])  # it cannot go ahead after staring from back string
# # print(parrot[-4:-2])    #Bl; -2 is upto not included
# # print(parrot[-4:12])    #Bl 12 is found before ending the string
# # print(parrot[4:-6])
# # print(parrot[4:-16])
# # print(parrot[4:2])
# # print(parrot[-18:6])
# # print(parrot[-14:-6])
#
# #                   1
# #         01234567890123
# parrot = "Norwegian Blue"
# print(parrot[0:6:2])
# print(parrot[0:6:3])
# print(parrot[-1:10:2])  # 3rd part is step of 2 characters means jump every 2nd char and so on...
#
# number = "1,234,567:890 123;456|445"
# print(number[1::2])
# print(number[1::3])
# #print(number[1::4])
#
# separators = number[1::4]
# print(separators)
#
# values = "".join(char if char not in separators else " " for char in number).split()
# print([int(val) for val in values])

print();
name = "Piyush"
age = 24
print(name + f" is {age} years old")    # f means format string similar to replacement string
print(f"Pi is approximately {22 / 7 : 12.50f}")
