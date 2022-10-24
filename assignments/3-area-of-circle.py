"""
Write a program that accepts the inputs for a circle's dimensions and calculates the area.
"""

from turtle import circle


print("Please enter the radius:")
radius = float(input())

circle_area = 3.14159265 * radius * radius

print('The area of a circle with radius of', radius, 'is', circle_area, '.')