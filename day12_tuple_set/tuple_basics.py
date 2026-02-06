# Tuple basics

# Creating a tuple
numbers = (10, 20, 30, 40)
print(numbers)

# Accessing elements
print(numbers[0])   # first element
print(numbers[2])   # third element

# Length of tuple
print("Length:", len(numbers))

# Looping through tuple
for n in numbers:
    print(n)

# Trying to modify tuple (this will give an error if uncommented)
# numbers[1] = 25
