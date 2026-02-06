# Set basics

# Creating a set (duplicates are removed automatically)
nums = {1, 2, 3, 2, 1}
print(nums)

# Adding elements to set
nums.add(4)
print("After adding 4:", nums)

# Removing elements from set
nums.remove(2)
print("After removing 2:", nums)

# Looping through set
for n in nums:
    print(n)

# Length of set
print("Length:", len(nums))
