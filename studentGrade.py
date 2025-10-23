#inputing 5 Sub marks and calulating grade and average.
marks = []
for i in range(1, 6):
    mark = int(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

average = sum(marks) / 5

# Determine grade based on average
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
elif average >= 50:
    grade = "E"
else:
    grade = "Fail"

print("Average Marks:", average)
print("Grade:", grade)
