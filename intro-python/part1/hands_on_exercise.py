"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print("type of pi", type(pi), "value=", pi)


# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i != 50:
    print (i)



# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit != 'orange':
    print ("picked fruit is ", picked_fruit)
else:
    print("orange")


# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def multiply_number(a,b):
    print (a , " x " , b , " = ", a*b)

multiply_number(2,3)

# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =", )

print("48 x 17 =", )

print("196523 x 87323 =", )
