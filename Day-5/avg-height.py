student_heights = input("Input a list of student heights ").split()
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

count = 0
total = 0

for student in student_heights:
    count=count+1
    total = total + student

average = round((total/count),2)

print(f"Average height is {average}")
