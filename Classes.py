###############################################################################
# Class member variables
###############################################################################
# Instructions
# Inside your Car class, replace the pass statement with a new member variable 
# named condition and give it an initial value of the string "new".

class Car(object):
    condition = "new"

my_car = Car()
###############################################################################
# Calling class member variables
###############################################################################
# Instructions
# At the end of your code, use a print statement to display the condition of 
# my_car.

class Car(object):
    condition = "new"

my_car = Car()

print my_car.condition
###############################################################################
# Initializing a class
###############################################################################
# Instructions
# Define the __init__() function of the Car class to take four inputs: self, 
# model, color, and mpg. Assign the last three inputs to member variables of 
# the same name by using the self keyword.
# Then, modify the object my_car to provide the following inputs at 
# initialization:
# model = "DeLorean"
# color = "silver"
# mpg = 88
# You don't need to include the self keyword when you create an instance of a 
# class, because self gets added to the beginning of your list of inputs 
# automatically by the class definition.

class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
        
my_car = Car("DeLorean", "silver", 88)

print my_car.condition
###############################################################################
# Referring to member variables
###############################################################################
# Instructions
# Now that you've created my_car print its member variables:
# 1) First print the model of my_car. Click "Stuck? Get a hint!" for an 
# example.
# 2) Then print out the color of my_car.
# 3) Then print out the mpg of my_car.

class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
        
my_car = Car("DeLorean", "silver", 88)

print my_car.model
print my_car.color
print my_car.mpg
###############################################################################
# Creating class methods
###############################################################################
# Instructions
# 1) Inside the Car class, add a method named display_car() to Car that will 
# reference the Car's member variables to return the string, "This is a 
# [color] [model] with [mpg] MPG." You can use the str() function to turn your 
# mpg into a string when creating the display string.
# 2) Replace the individual print statements with a single print command that 
# displays the result of calling my_car.display_car()

class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    
    def display_car(self):
        return "This is a" + " " + self.color + " " + self.model + " with" + " " + str(self.mpg) + " MPG."

my_car = Car("DeLorean", "silver", 88)
print my_car.display_car()
###############################################################################
# Modifying member variables
###############################################################################
# Instructions
# 1) Inside the Car class, add a method drive_car() that sets self.condition 
# to the string "used".
# 2) Remove the call to my_car.display_car() and instead print only the 
# condition of your car.
# 3) Then drive your car by calling the drive_car() method.
# 4) Finally, print the condition of your car again to see how its value 
# changes.

class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    
    def display_car(self):
        return "This is a" + " " + self.color + " " + self.model + " with" + " " + str(self.mpg) + " MPG."
        
    def drive_car(self):
        self.condition = "used"

my_car = Car("DeLorean", "silver", 88)

print my_car.condition

my_car.drive_car()

print my_car.condition
###############################################################################
# Inheritance
###############################################################################
# Instructions
# Create a class ElectricCar that inherits from Car. Give your new class an 
# __init__() method of that includes a "battery_type" member variable in 
# addition to the model, color and mpg.
# Then, create an electric car named "my_car" with a "molten salt" 
# battery_type. Supply values of your choice for the other three inputs 
# (model, color and mpg).

class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    
    def display_car(self):
        return "This is a" + " " + self.color + " " + self.model + " with" + " " + str(self.mpg) + " MPG."
        
    def drive_car(self):
        self.condition = "used"
    
class ElectricCar(Car):
    def __init__(self, battery_type):
        self.battery_type = battery_type
        
my_car = ElectricCar("molten salt")
my_car.model = "Delorean"
my_car.color = "Silver"
my_car.mpg = 88
###############################################################################
# Overriding methods
###############################################################################
# Instructions
# 1) Inside ElectricCar add a new method drive_car() that changes the car's 
# condition to the string "like new".
# 2) Then, outside of ElectricCar, print the condition of my_car
# 3) Next, drive my_car by calling the drive_car() function
# 4) Finally, print the condition of my_car again

class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    
    def display_car(self):
        return "This is a" + " " + self.color + " " + self.model + " with" + " " + str(self.mpg) + " MPG."
        
    def drive_car(self):
        self.condition = "used"
    
class ElectricCar(Car):
    def __init__(self, battery_type):
        self.battery_type = battery_type
    
    def drive_car(self):
        self.condition = "like new"
        
my_car = ElectricCar("molten salt")
my_car.model = "Delorean"
my_car.color = "Silver"
my_car.mpg = 88

print my_car.condition
my_car.drive_car()
print my_car.condition
###############################################################################
# Building useful classes
###############################################################################
# Instructions
# 1) Define a Point3D class that inherits from object
# 2) Inside the Point3D class, define an __init__() function that accepts 
# self, x, y, and z, and assigns these numbers to the member variables 
# self.x, self.y, self.z
# 3) Define a __repr__() method that returns "(%d, %d, %d)" % 
# (self.x, self.y, self.z). This tells Python to represent this object in the 
# following format: (x, y, z).
# 4) Outside the class definition, create a variable named my_point containing 
# a new instance of Point3D with x=1, y=2, and z=3.
# 5) Finally, print my_point.

class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

my_point = Point3D(1, 2, 3)

print my_point
###############################################################################
