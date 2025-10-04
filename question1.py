marks = []   

for i in range(1, 6):
    m = int(input(f"Enter marks for subject {i}: "))
    marks.append(m)


total = sum(marks)
average = total / 5


if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "Fail"

# Output
print("\n--- Result ---")
print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)