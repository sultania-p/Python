age = int(input("How old are you? "))

if (age>=18 and age <=40):
    print("You are a youth")
elif (age < 18):
    print("You are a minor")
else:
    print("You are a senior citizen")

# Simplify Chained Comparison
if 18 <= age <= 40:
    print("You are a youth")
elif age < 18:
    print("You are a minor")
else:
    print("You are a senior citizen")
print("-" * 80)
print()


# Always use parenthesis while using mixed boolean operators




