a = 12
b = 2

# below are examples of expressions
print('a+b' + ' = ' + str(a+b))
print('a-b' + ' = ' + str(a-b))
print('a*b' + ' = ' + str(a*b))
print('a/b' + ' = ' + str(a/b))         # gives decimal output
print('a // b' + ' = ' + str(a//b))     # integer division - rounded down towards minus infinity
print('a % b' + ' = ' + str(a%b))       # modulo : the remainder of the division

print()

for i in range(1, 4):
    print(i)
#for i in range(1, a/b): # float as a/b is 4.0 can be used int only not float
    #print(i)
for i in range(1, a//b):
    print(i)

# whatever is needed to be evaluated by Python will be an expression
# like range( is an expression, 1 and a//b is an expression too
# i is an expressions as it will have to be valued from 1 to 4
# a and b are not expressions as those values are bound with == sign

print()

print(a + b / 3 - 4 * 3)
