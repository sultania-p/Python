shopping_list = ["milk", "pasta", "eggs", "spam", "rice", "noodles", "spam"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

# for item in shopping_list:
#     if item == "spam":
#         continue # case the existing following commands to be skipped!
#
#     print("Buy " + item)

# for item in shopping_list:
#     if item == "spam":
#         break   # not looking further if we find what we want! break terminate the process
#
#     print("Buy " + item)
# ## --
# print()

items_to_find = "spam"
found_at = None

# len_list = len(shopping_list)
# for item in range(len_list):
#     if shopping_list[item] == items_to_find:
#         found_at = item
#         break
#
# if found_at is not None:
#     print("Item is found at position {0}".format(found_at))
# else:
#     print("{} is not found!".format(items_to_find))

if items_to_find in shopping_list:
    found_at = shopping_list.index(items_to_find)

if found_at is not None:
    print("Item is found at position {0}".format(found_at))
else:
    print("{} is not found!".format(items_to_find))