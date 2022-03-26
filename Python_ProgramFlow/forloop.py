# country = "United States of America"
#
# for character in country:
#     print(character)

# number = "9,234,456,445;978 345:767"
# separators = ""
#
# for char in number:
#     if not char.isnumeric():
#         separators = separators + char
#
# print(separators)
# values = "".join(char if char not in separators else " " for char in number).split()
# print([int(val) for val in values])

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
# capital = ""
# # Use a for loop and an if statement to print just the capitals in the quote above.
# for char in quote:
#     if char.isupper():
#         capital = capital + char
# print(capital)

# for i in range(1,20):
#     print("i is now having the value of {} ".format(i))
#
# for i in range(0,10):
#     print(i)

for i in range(10,2):   # 10 is starting index and 0 is ending index
    print(i)

for i in range(0,10,2):
    print(i)