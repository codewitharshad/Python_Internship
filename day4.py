print("Hello Welcome To Python \n Hello Dear \t hello ")


# Type casting- convert one data type into another

age=int("20")

print(age)
print(type(age))

# str()
# float()
# bool()

a=20
b="30"

print(a+int(b)) #error


empId=float(1234)
print(empId)

print(type(empId))


###########################################################

# String concatenation

# +
# ,
# f""- modern and easy - recommended


name="Aditya"
skill="Python"

print("Your name Is: ",name)
print("Your Skill Is "+name)


# number1=100
# number2=23
# print(number1+number2)


# number1=100
# number2="23"
# print(type(number1))
# print(type(number2))
# print(number1+number2)


# number1=str(100)
# number2=int(23)
# print(type(number1))
# print(type(number2))
# print(number1+number2)

# , - most useful for merging or concat
# automatically convert into strings

no1=230
no2="20"
print(no1,no2)


empRole="Python Full Stack Engineer"
empAddress='Pune'


print("Your Role is "+empRole+"Your Address is "+empAddress)
print('Your Role is ',empRole, "Your Address is ",empAddress)


# #################

# f""

empAge=30
empCTC="20 LPA"


print(f"Your Age is {empAge} and empCTC is {empCTC}")



age="20"
name="Sanmesh"
skill="MERN"
role="Deveoloper"

print("Your Age : "+age+" Name Is"+name+"Skill is "+skill+" Role Is "+role)

print("Your Age : ", age, " Name Is",name,"Skill is ",skill," Role Is ",role)

print(f"Role Is {role} and skill is {skill} , age is {age}. and name is {name}")


# ********************************************************

# Take input from user
# input()- return data in a string

# name="Pratik"
name=input("enter your name ")
print("Your name is ",name)



# **********************************

a=int(input("Enter Number 1. "))
b=int(input("Enter Number 2. "))

print("Sum is ", a+b) # 2030




# *******************************

# Python reserved keywords

# True
# False
# if

# print
# input
# type

import keyword
print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 
# 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 
# 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import',
#  'in', 'is', 'lambda', 
# 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


# id - to check memory location  of variable

x=20
print(x)
print(id(x))

b=30
print(id(b))
print(b)