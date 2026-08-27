print("====== STUDENT GRADE CALCULATOR ======")

def get_total(marks):
    return sum(marks)


def get_percentage(total, number_of_subjects):
    return total / number_of_subjects


def get_grade(percentage):
    if percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


# Taking student information
name = input("Enter student name: ")

marks = []

number_of_subjects = int(input("Enter number of subjects: "))

for i in range(number_of_subjects):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)


# Calling functions
total = get_total(marks)
percentage = get_percentage(total, number_of_subjects)
grade = get_grade(percentage)


# Display result
print("\n====== RESULT ======")
print("Student:", name)
print("Marks:", marks)
print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)