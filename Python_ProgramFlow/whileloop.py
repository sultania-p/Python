for i in range(10):
    print("i is now {0}".format(i))

i = 0   # initialization
while i<10:
    print("i is now {0}".format(i))
    i += 1 # increment in i

##
available_exits = ["east", "west", "north", "south"]
chose_exit = ""

while chose_exit not in available_exits:
    chose_exit = input("Please chose an exit direction: ")

print("You chose the correct exit direction! Congratulations on getting out from dungeon!")


