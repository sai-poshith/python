# Dictionary looping examples

student = {
    "name": "Sai",
    "age": 22,
    "branch": "CSE",
    "college": "ABC College"
}

# Loop through keys
print("Keys:")
for key in student:
    print(key)

print()

# Loop through values
print("Values:")
for value in student.values():
    print(value)

print()

# Loop through key-value pairs
print("Key - Value pairs:")
for key, value in student.items():
    print(key, ":", value)

# Length of dictionary
print("\nTotal keys:", len(student))
