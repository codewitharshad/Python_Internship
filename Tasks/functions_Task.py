
# Task 1 – Function to find square of a number
def square_number(n):
    return n * n


# Task 2 – Function to return max of 3 numbers
def max_of_three(a, b, c):
    return max(a, b, c)


# Task 3 – Function to calculate factorial (using loop)
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Task 4 – Function to check even or odd
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Task 5 – Function to print multiplication table
def multiplication_table(n):
    for i in range(1, 11):
        print(n * i)


# Task 6 – Function to count vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


# Task 7 – Recursive function for countdown
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)


# Task 8 – Function with default parameter
def greet(name="Guest"):
    print("Hello", name)


# Task 9 – Function returning both sum and average
def sum_and_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average


# Task 10 – Function using *args to calculate total marks
def total_marks(*marks):
    return sum(marks)
