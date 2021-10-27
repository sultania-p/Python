number = 5

print("Please enter the number between 1 and 10: ")
guess = int(input())

# if (guess > number):
#     print("Please guess lower")
# elif (guess < number):
#     print("Please guess higher")
# else:
#     print("Guessed the correct number")

# if (guess < number):
#     print("Please guess higher")
#     guess = int(input())
#     if (guess == number):
#         print("Guessed correctly!")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif (guess > number):
#     print("Please guess lower")
#     guess = int(input())
#     if (guess == number):
#         print("Guessed correctly!")
#     else:
#         print("Sorry, you have not guessed correctly!")
# else:
#     print("You have guessed correctly!")

# if (guess != number):
#     if (guess < number):
#         print("Please guess higher")
#     else:   # Guess must be lower than the number
#         print("Please guess lower")
#     guess = int(input())
#     if (guess == number):
#         print("You got it correct this time!")
#     else:
#         print("Sorry, you guessed it incorrectly!")
# else:
#     print("You guessed it right first time")

if (guess == number):
    print("You guessed it right first time")

else:
    if (guess < number):
        print("Please guess higher")
    else:   # Guess must be lower than the number
        print("Please guess lower")
    guess = int(input())
    if (guess == number):
        print("You got it correct this time!")
    else:
        print("Sorry, you guessed it incorrectly!")