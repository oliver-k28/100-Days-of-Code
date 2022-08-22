#calculates average student heights
#example input: 156 187 167 171 193 145


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


students = 0
for student in student_heights:
    students += 1


total = 0
for student in student_heights:
    total += student
average_height = (total / students)
print(round(average_height))

