phy = int(input("Enter Physics marks: "))
chem = int(input("Enter Chemistry marks: "))
bio = int(input("Enter Biology marks: "))
maths = int(input("Enter Maths marks: "))
comp = float(input("Enter Computer marks: "))


total_marks = phy + chem + bio + maths + comp
percentage = (total_marks / 500) * 100


if percentage >= 90:
    grade = "Grade A"
elif percentage >= 80:
    grade = "Grade B"
elif percentage >= 70:
    grade = "Grade C"
elif percentage >= 60:
    grade = "Grade D"
elif percentage >= 40:
    grade = "Grade E"
else:
    grade = "Grade F"


print("Percentage: {percentage}%")
print("Grade: {grade}")
