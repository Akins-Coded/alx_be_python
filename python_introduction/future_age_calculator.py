score = int(input("Enter the Student's Score: "))
if score >= 90:
  grade = "A"
elif score >= 80:
  grade = "B"
elif score >= 70:
  grade = "C"
elif score >= 50:
  grade = "D"
else:
  grade = "F"

print("Your grade is:", grade)