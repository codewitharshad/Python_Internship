
# Arithmatic operators


# a+b=
# a,b-opearand
# += operator


a=100
b=20
print(a+b) # 120
print(a*b) # 2000
print(a-b) # 80
print(a/b) # divide by - return quotient. # 5
print(a%b) # mod- return reminder value. # 0

print(2**3) # return power - 2^3 - 8
print(5**3) # 125



# BODMAS Rule
# higher priority-() => then =>  / % * => then => + -

print(a*b+a) # 2000+100=2100
print(a+b/a) #  b/a= 20/100 = 100.2
print(a*b/a) # 2000 / 100 = 20
print(a+(b*a)) #2000 + 100


# *************************************************************


# comparsion Operator- used to compare 2 values and return boolean value 
# ==, !=,>,<,>=,<=
x=20
y=30
print(x==y) # False

print(x!=y) #True

print(x>y) # False
print(x>=y) # False


print(x<=y) # True


print(20!=20) # False
print(20=="20") # False

# **********************************

# Logical Operator

# used to handle 2 or more conditions at a same time

# && ||  ! - other langauge
# and , or , not - In python


# 1- True
# 0-False

# and

# all conditions must be true

# 1 and 1 =1
# 1 and 0 = 0
# 0 and 1=0
# 0 and 0 =0


P=200
Q=300
R=500

print(P>=Q and P<=R) # False



# OR- any one condition must be true

# 1 or 1=1
# 1 or 0=1
# 0 or 1 =1
# 0 or 0=0

print(P<=Q or Q<=R) # True || True = true


# not

print(not(10<2)) # True

###########################################

# Assignment Operator
# LSV=RSV
# = , +=,-=,/=, %=

a=20
b=a
print(a,b)

no1=20
no2=40

print(no1+no2) # 60
no1+=no2 # no1=no1+no2
print(no1) # 60
print(no2) #40
no1*=no2 # no1=no1*no2 =  60*40 //2400
print(no1) # 2400
print(no2) # 40

no2-=no1 # no2=no2-no1 = 40-2400 = 2360

print(no1)# 2400
print(no2) # -2360


#############################

# Bitwise Op.

# Bitwise & 
# Bitwise |
# bitwise XOR ^
# bitwise ~
# >>
# <<
# >>>
# <<<

# COnvert into Decimal into binary

print(5 & 3) # 1

# 5-0101
# 8       4       2     1.  Rule



# 0       1.      0.    1
# 0       0.      1.    1
# *************************
#   0.      0.      0.    1- binary - decimal-  1



print(5 & 8) # 0

#  =>8421
#  5=0101
#  8=1000
# ********
# 0000- decimal- 0





# **********************************

# Ternary Operator

# in other language - condition ?  if true : if false


# In python- result="if true" if condition else "if false"

age=int(input("Enter Your Age"))
result="Congrats bro " if age>=18 else "Sorry dear"
print(result)
