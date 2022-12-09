print("Please enter the number of students in the class:")
number_of_students = int(input())

print("Please enter the students' grades (in separate lines):")

grades_sum = 0

for i in range(number_of_students):
    curr_grade = int(input())
    grades_sum += curr_grade

average = grades_sum / number_of_students
print("The class average is", average)

## Can also rewrite when the total number of students isn't known.

"""
while(seen_done == false)
    <Do Something>
"""