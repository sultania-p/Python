# value = "Supernatural Phenomenon"
#
# letter = input("Please enter the character: ")
# if letter in value:
#     print("{} is contained in {}".format(letter,value))
# else:
#     print("The character is not present in the value")
#
# activity = input("What would you like to do today? ")
# if "cinema" not in activity.casefold():     # Casefold/lower will make the string in lower case
#     print("I don't want to {}, I want to go to movie".format(activity))
# else:
#     print("Yay! It's movie time!")
#
# stringval = "United States"
# print(stringval.find("t"))
# print(stringval.count("t"))

name = input("Please enter the name: ")
age = int(input("Please enter the age: "))

print(age)
if name != "" and age is not None:
    if 18 < age < 31:
        print("Welcome to the holiday, {}".format(name))
    else:
        print("Sorry, you are not eligible for the trip!")
else:
    print("Please enter the name and age to check for eligibility!")