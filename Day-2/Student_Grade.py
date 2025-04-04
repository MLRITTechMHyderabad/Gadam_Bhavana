# List of students with their grades
students = [
    ("Alice", [85, 90, 78, 92]),
    ("Bob", [60, 65, 70, 75]),
    ("Charlie", [40, 45, 50, 55]),
    ("David", [90, 74, 82, 67])
]

# Creating an empty dictionary to store student grades
grades_dict = {}

# Storing student names as keys and their grades as values
for student in students:
    name = student[0]
    grades = student[1]
    grades_dict[name] = grades

# Printing the dictionary
print("Student Grades Dictionary:", grades_dict)

# Creating a dictionary to store average grades
averages = {}
pass_count = 0
highest_avg = 0
top_student = ""

# Calculating average grades and finding the highest average
for name in grades_dict:
    total = sum(grades_dict[name])
    count = len(grades_dict[name])
    avg = total / count
    averages[name] = avg
    print("Average of", name, "is:", avg)

    # Checking for the highest average
    if avg > highest_avg:
        highest_avg = avg
        top_student = name

    # Counting passed students
    if avg >= 50:
        pass_count += 1

# Printing final results
print(top_student, "got the highest average.")
print("Number of students who have passed:", pass_count)
