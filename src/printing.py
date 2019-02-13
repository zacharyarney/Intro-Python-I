"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("\n==printf operator==\n")
print("x is %d, y is %.5f, z is '%s'" % (x, y, z))

# Use the 'format' string method to print the same thing
print("\n==format string method==\n")
print("x is {}, y is {}, z is '{}'".format(x, y, z))

# Finally, print the same thing using an f-string
print("\n==f-string==\n")
print(f"x is {x}, y is {y}, z is '{z}'")