student_scores = input("Imput a list of student scores ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max = 0

for score in student_scores:
    if(score>max):
        max = score

print(f"Highest score in class is {max}")