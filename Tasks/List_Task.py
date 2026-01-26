
# Task 1 – Create a list of 5 subjects and print them one by one
subjects = ["Maths", "Physics", "Chemistry", "Biology", "English"]

for subject in subjects:
    print(subject)


# Task 2 – Add a new subject in the middle using insert()
subjects.insert(2, "Computer Science")
print(subjects)


# Task 3 – Remove one subject using remove()
subjects.remove("Biology")
print(subjects)


# Task 4 – Sort the list alphabetically
subjects.sort()
print(subjects)


# Task 5 – Create a list [1,2,3,4,5] and print their squares using list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]
print(squares)


# Task 6 – Create a nested list of students and print the 2nd student’s name
students = [
    ["Shivam", 21],
    ["Amit", 22],
    ["Rahul", 20]
]

print(students[1][0])
