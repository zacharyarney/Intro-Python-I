# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE 
x.append(4)
print("\n==APPENDS 4==\n")
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE 
x.extend(y)
print("\n==EXTENDS y==\n")
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE 
x.remove(8)
print("\n==REMOVES 8==\n")
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE 
x.insert(5, 99)
print("\n==INSERTS 99==\n")
print(x)

# Print the length of list x
# YOUR CODE HERE 
print("\n==LENGTH==\n")
print(len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
new_x = [n * 1000 for n in x]
print("\n==x1000==\n")
print(new_x)
print("\nor\n")
for n in x:
    print(n * 1000) 