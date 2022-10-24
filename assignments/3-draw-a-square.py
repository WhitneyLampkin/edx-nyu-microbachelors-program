"""
Write a program that reads from the user the length of a side of a square,
and draws a square of that size.
"""

"""
Python doesn't support drawing.
So the Turtle Graphics Module will be used.
"""
import turtle

print('Please enter the length of each side:')
side = int(input())

turtle.forward(side)
turtle.left(90)
turtle.forward(side)
turtle.left(90)
turtle.forward(side)
turtle.left(90)
turtle.forward(side)
turtle.left(90)

turtle.hideturtle()
turtle.done()