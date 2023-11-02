# Method 1:
students = ["Sam", "Alice", "Mona"]
subjects = ["Commerce", "Science", "Computer"]

student_subject_dict = {}  

for student, subject in zip(students, subjects):
    student_subject_dict[student] = subject

print(student_subject_dict)



# Method 2

students = ["Sam", "Alice", "Mona"]
subjects = ["Commerce", "Science", "Computer"]

student_subject_dict = {student: subject for student, subject in zip(students, subjects)}

print(student_subject_dict)
