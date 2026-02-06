# Remove duplicates from a list using set

numbers = [1, 2, 2, 3, 1, 4, 5, 4]
print("Original list:", numbers)

# Convert list to set (removes duplicates)
unique_numbers = set(numbers)
print("Unique values (set):", unique_numbers)

# Convert back to list if needed
unique_list = list(unique_numbers)
print("Unique list:", unique_list)
