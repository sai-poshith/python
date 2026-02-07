# Append data to a file

file = open("data.txt", "a")

file.write("\nThis line is appended")
file.write("\nLearning Python is fun")

file.close()

print("Data appended to file")
