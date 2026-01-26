

# OOP_ is of professional way of writing our code to solve real world problmens

# like- Avoid Code Reptition
# Securtity and Proetection
# Easy Maintainance
# Oragnaized Code

# OOP 4 Pillars
# Inhertiance
# Polymorphim
# Encapsulation
# Asbtraction

# OOP has class and Objects

# Class- is a real time entity having methods and properties
        # is a blueprint of a object

# eg- class Mobile- class
        #   Properties / attributes/ variables - name,color,brand,ram,rom,
        # methods/ action/ function - calling, switchon,switchoff,chatting
 
 
# object- instance of a class
# eg we can create 1000 of mobile by using same mobile class 


# # creating clas
# class Mobile:
#     pass


# # creating object
# m1=Mobile()
# m2=Mobile()

# *************************

# eg

class Mobile:
    # properties / variables
    name="Iphone 18 pro"
    brand="Apple"
    color="Midnight Black"

    # methods
    def calling(self):
        print("hello i am busy on call.....")
    
    def chatting(self):
        print("i am chatting with someone...")

    def camera(self):
        print("CLicking photos....")


m1=Mobile()
print(m1.name)
print(m1.brand)

m1.calling()
m1.chatting()
m1.camera()





     
