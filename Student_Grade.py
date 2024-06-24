student_records = []

number_of_students = int(input("Please Enter the number of students in a class :"))

for student_number in  range(number_of_students) : 
    student_name = input(f"Enter the name of the student {student_number} :")
    student_grades = []
    for grades in range(1,6):
        marks = int(input(f'Enter the marks for subject {grades}:'))
        student_grades.append(marks) 
    student_records.append([student_name,student_grades])

       

total_class_marks = 0

for student in student_records:
    student_n, student_g = student
    
    student_average = sum(student_g)/len(student_g)
    total_class_marks+= student_average
    print(f"Name of the student{student_n}")
    print(f"Grades: {student_g}")
    print(f"Average of a student : {student_average:.2f}")


