# Student Marks Manager

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

# Save to file
with open("data.txt", "w") as file:
    for name, marks in students.items():
        file.write(name + "," + str(marks) + "\n")

print("\nData saved to file.\n")

# Read from file and display result
with open("data.txt", "r") as file:
    for line in file:
        name, marks = line.strip().split(",")
        marks = int(marks)

        if marks >= 50:
            result = "Pass"
        else:
            result = "Fail"

        print(name, ":", marks, "-", result)
