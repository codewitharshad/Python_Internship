
# Task 1 – Handle division by zero
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")


# Task 2 – Ask for age and handle invalid input
try:
    age = int(input("Enter your age: "))
    print("Age:", age)
except ValueError:
    print("Invalid age input")


# Task 3 – Create a calculator using try–except
try:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    op = input("Enter operator (+ - * /): ")

    if op == "+":
        print(x + y)
    elif op == "-":
        print(x - y)
    elif op == "*":
        print(x * y)
    elif op == "/":
        print(x / y)
    else:
        print("Invalid operator")
except ZeroDivisionError:
    print("Division by zero error")
except ValueError:
    print("Invalid number input")


# Task 4 – Read a file safely using exception handling
try:
    file = open("sample.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File not found")


# Task 5 – Validate password length
try:
    password = input("Enter password: ")
    if len(password) < 6:
        raise ValueError("Password too short")
    print("Password accepted")
except ValueError as e:
    print(e)


# Task 6 – Function that only accepts positive numbers
def positive_number(n):
    if n <= 0:
        raise ValueError("Only positive numbers allowed")
    return n

try:
    print(positive_number(int(input("Enter a number: "))))
except ValueError as e:
    print(e)


# Task 7 – Login system with custom error
class UserNotFoundError(Exception):
    pass

users = ["admin", "shivam", "user1"]

try:
    username = input("Enter username: ")
    if username not in users:
        raise UserNotFoundError("Username not found")
    print("Login successful")
except UserNotFoundError as e:
    print(e)
