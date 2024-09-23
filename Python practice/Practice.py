# this is for practice only and is broken down into various chunks

# tutorial for beginners

# This is my first Python program Lesson 1
print("I Like Kebab!")
print("It's really good!")



# Lesson 2: Variables

# Variable = A container for a value  (string, interger, float, boolean)
# A variable behaves as if it was the value it contains

# Strings
first_name = "Karan"
food = "pizza"
email = "karanjeet1612@outlook.com"

print(f"My name is {first_name}")
print(f"I like {food}")
print(f"My email is {email}")

# Integers
age = 21
quantity = 3
num_of_students = 30

print(f"I am {age} years old")
print(f"I am buying {quantity} items")
print(f"My class has {num_of_students} students")

# Floats
price = 10.99
degree = 1
distance = 6

print(f"The price is ${price}")
print(f"My Degree is: {degree}st class")
print(f"Today I ran {distance} miles")

# Booleans
# booleans are always capital
is_student = False
for_sale = True
is_online = True

if is_online:
    print("You are online")
else: 
    print("You are offline")


# Lesson 3: type casting

# Typecasting = the process of converting a variable from one data type to another
#    str(), int(), float(), bool()

name = "Karanjeet Singh"        #str
age = 21                        #int
gpa = 5.2                       #float
is_student = True               #bool

gpa = int(gpa)                  #converts float to int

print(gpa)4


age = str(age)                  # this is not a string not an int

print(age)


name = bool(name)           #can be used to check if someones    entered thier name
print(name)


# Lesson 4: user input

# input() = A function that prompts the user to enter data
#           RReturns the entered data as a string

name = input("What is your name?: ")
age = int(input("how old are you?: "))

age = age + 1

print(f"Hello {name}!")     #f strings are used to insert a variable
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old") 

# area of a rectangle
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width

print(f"The area is: {area}cm²")   # alt + 0178 gives 2

# shopping cart
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} of {item}s")
print(f"Your total is ${total}")


# Lesson 5: Madlibs games

# Madlibs game
# word game where you create a story by filling in the blanks with random words

adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place, thing): ")
adjective2 = input("Enter an adjective (description): ")
verb1 = input("Enter a verb ending with 'ing': ")
adjective3 = input("Enter an adjective (description): ")

print(f"Today I went to a {adjective1} Zoo.") # Adjective is a describing word
print(f"In an exhibit, I saw a {noun1}") # noun is a person place object
print(f"{noun1} was {adjective2} and {verb1}") # verb is an action
print(f"I was {adjective3}!")


# Lesson 6: arthmatic & maths

friends = 5

#friends = friends + 1
#friends += 1       #augmented assignment operators
#friends = friends - 2
#friends -= 2       #augmented assignment operators
#friends = friends * 3
#friends *= 3       #augmented assignment operators
#friends = friends / 2
#friends /= 2        #augmented assignment operators
#friends = friends ** 2 #to the power of
#friends **= 2       #augmented assignment operators
remainder = friends % 3


#print(friends)
print(remainder)



x = 3.14
#y = -4
y = 4
z = 5

#result = round(x)
#result = abs(y)         # absolute value
#result = pow(4, 3)       # power
result = max(x, y, z)       #gets the biggest or smallest number
result = min(x, y, z)


print(result)

# maths import
import math

x = 9.1

#print(math.pi)
#print(math.e)
#result = math.sqrt(x)
#result = math.ceil(x)   #rounds up
result = math.floor(x) #rounds down

print(result)

# circumference
import math

radius = float(input("Enter the radius of a circle:"))

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}cm") #rounds to 2 digits

# area of a circle
import math

radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(area, 2)}cm²")

#calculate hypotenuse
import math

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))  #2 is the power

print(f"The hypotenuse is: {round(c)}cm")



# Lesson 7: if statements

# if = Do some code only IF some condition is True
#      Else do something else

age = int(input("Enter your age: "))

if age >= 100:
    print("You are dead")
elif age >= 18:
    print("You are eligible!")
elif age < 0:
    print("You haven't been born yet!")
else: 
    print("You must be 18 or over!")