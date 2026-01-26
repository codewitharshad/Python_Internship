

# Task 1 – Print numbers 1 to 10 using a for loop
for i in range(1, 11):
    print(i)

# ***********************************************************************************************************************

# Task 2 – Print even numbers 1 to 20
for i in range(2, 21, 2):
    print(i)

# ***********************************************************************************************************************

# Task 3 – Positive, negative, or zero check
n = int(input())
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

# ***********************************************************************************************************************

# Task 4 – Print your name 5 times
for _ in range(5):
    print("Shivam")
    
# ***********************************************************************************************************************

# Task 5 – Sum of numbers 1 to 100
print(sum(range(1, 101)))

# ***********************************************************************************************************************

# Task 6 – Multiplication table of a number
n = int(input())
for i in range(1, 11):
    print(n * i)
    
# ***********************************************************************************************************************

# Task 7 – Check if divisible by 5 and 11
n = int(input())
if n % 5 == 0 and n % 11 == 0:
    print("Divisible")
else:
    print("Not Divisible")
    
# ***********************************************************************************************************************

# Task 8 – Reverse numbers 10 → 1
for i in range(10, 0, -1):
    print(i)
    
# ***********************************************************************************************************************

# Task 9 – Find largest of 3 numbers
a = int(input())
b = int(input())
c = int(input())
print(max(a, b, c))

# ***********************************************************************************************************************

# Task 10 – Password validation loop until "python123"
while True:
    p = input()
    if p == "python123":
        print("Access Granted")
        break

# ***********************************************************************************************************************

# Task 11 – Fibonacci series
n = int(input())
a, b = 0, 1
for _ in range(n):
    print(a)
    a, b = b, a + b
    
# ***********************************************************************************************************************

# Task 12 – Prime number check
n = int(input())
if n > 1 and all(n % i != 0 for i in range(2, n)):
    print("Prime")
else:
    print("Not Prime")
    
# ***********************************************************************************************************************

# Task 13 – Menu-driven calculator using match-case
a = int(input())
b = int(input())
op = input()

match op:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)
