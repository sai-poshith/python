# Save marks to a file
with open("marks.txt", "w") as file:
    for i in range(3):
        m = input("Enter marks: ")
        file.write(m + "\n")
# Read marks from file
with open("marks.txt", "r") as file:
    for line in file:
        print("Marks:", line.strip())
