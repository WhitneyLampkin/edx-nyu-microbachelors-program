"""
Write a program that reads from the user the length of the two legs in a right triangle,
and draws such a triangle.
"""

import math
import turtle


print("Please enter the length of the two legs in a right triangle:")

a = int(input("Leg #1: "))
b = int(input("Leg #3: "))

c = math.sqrt(a**2 + b**2)
alpha_in_radians = math.atan(a/b)
alpha = math.degrees(alpha_in_radians)

turtle.forward(a)
turtle.left(90)
turtle.forward(b)
turtle.left(180 - alpha)
turtle.forward(c)
turtle.hideturtle()
turtle.done()