# Task 1 – Create a dictionary of personal information
person = {
    "name": "Shivam",
    "age": 21,
    "city": "Nagpur",
    "skills": ["Python", "SQL", "OOP"]
}


# Task 2 – Print all keys and all values separately
print(person.keys())
print(person.values())


# Task 3 – Add a new key 'email' and update city
person["email"] = "shivam@example.com"
person["city"] = "Pune"
print(person)


# Task 4 – Delete the 'age' key
del person["age"]
print(person)


# Task 5 – Create a nested dictionary of two students
students = {
    "student1": {
        "name": "Amit",
        "age": 22
    },
    "student2": {
        "name": "Rahul",
        "age": 21
    }
}

print(students)


# Task 6 – Check if key 'skills' exists
if "skills" in person:
    print("skills key exists")
else:
    print("skills key does not exist")


# Task 7 – Use a loop to print all key–value pairs
for key, value in person.items():
    print(key, ":", value)