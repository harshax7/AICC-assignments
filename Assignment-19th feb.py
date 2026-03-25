students = {}
for i in range(5):
    name = input(f"Enter name of student {i+1}: ")
    marks = float(input(f"Enter marks of {name}: "))
    
    students[name] = marks
topper = max(students, key=students.get)
top_marks = students[topper]
average = sum(students.values()) / len(students)
def assign_grade(mark):
    if mark >= 90:
        return 'A'
    elif mark >= 75:
        return 'B'
    elif mark >= 50:
        return 'C'
    else:
        return 'F'
print("\n--- Student Details ---")
for name, marks in students.items():
    grade = assign_grade(marks)
    print(f"{name}: Marks = {marks}, Grade = {grade}")

print("\n--- Summary ---")
print(f"Topper: {topper} with {top_marks} marks")
print(f"Class Average: {average:.2f}")

# Output
# Enter name of student 1: Sneha
# Enter marks of Sneha: 92
# Enter name of student 2: Rahul
# Enter marks of Rahul: 78
# Enter name of student 3: Ananya
# Enter marks of Ananya: 85
# Enter name of student 4: Kiran
# Enter marks of Kiran: 60
# Enter name of student 5: Meera
# Enter marks of Meera: 45

# --- Student Details ---
# Sneha: Marks = 92.0, Grade = A
# Rahul: Marks = 78.0, Grade = B
# Ananya: Marks = 85.0, Grade = B
# Kiran: Marks = 60.0, Grade = C
# Meera: Marks = 45.0, Grade = F

# --- Summary ---
# Topper: Sneha with 92.0 marks
# Class Average: 72.00